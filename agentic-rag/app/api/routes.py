import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from .schemas import QueryRequest, QueryResponse
from .deps import get_agent_instance
from app.ingestion.pipeline import ingest_directory


router = APIRouter()

UPLOAD_DIR = "data/raw_docs"


@router.get("/")
def root():
    return {"message": "Agentic RAG API running"}


@router.post("/query", response_model=QueryResponse)
def query_docs(payload: QueryRequest):
    """
    Ask a question to the Agentic RAG system
    """

    try:
        agent = get_agent_instance()

        result = agent.invoke({"input": payload.question})

        return QueryResponse(answer=result["output"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ingest")
async def ingest_file(file: UploadFile = File(...)):
    """
    Upload a document and re-index vector DB
    Supports: pdf, txt, docx, xlsx, pptx
    """

    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        # save file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # run ingestion pipeline
        ingest_directory(UPLOAD_DIR)

        return {
            "status": "success",
            "filename": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
