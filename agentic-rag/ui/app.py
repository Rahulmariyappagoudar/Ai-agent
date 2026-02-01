import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Agentic RAG", layout="centered")
st.title("📚 Agentic RAG Assistant")

if "history" not in st.session_state:
    st.session_state.history = []


# =====================================================
# Upload Section
# =====================================================

st.subheader("Upload Document")

uploaded_file = st.file_uploader(
    "Upload PDF / TXT / DOCX / XLSX / PPTX",
    type=["pdf", "txt", "docx", "xlsx", "pptx"]
)

if uploaded_file:
    try:
        with st.spinner("Uploading & indexing..."):
            r = requests.post(
                f"{API_URL}/ingest",
                files={"file": (uploaded_file.name, uploaded_file.getvalue())}
            )

        data = r.json()

        if r.status_code == 200:
            st.success(f"{data['filename']} ingested successfully")
        else:
            st.error(data.get("detail", "Upload failed"))

    except Exception as e:
        st.error(f"Connection failed: {e}")


st.divider()


# =====================================================
# Ask Section
# =====================================================

st.subheader("Ask a Question")

question = st.text_input("Type your question")

if st.button("Ask") and question.strip():

    try:
        with st.spinner("Thinking..."):
            r = requests.post(
                f"{API_URL}/query",
                json={"question": question}
            )

        data = r.json()

        if r.status_code != 200:
            st.error(data.get("detail", "Server error"))
        else:
            answer = data.get("answer", "No answer returned")
            st.session_state.history.append((question, answer))

    except Exception as e:
        st.error(f"Connection failed: {e}")


# =====================================================
# Chat History
# =====================================================

for q, a in reversed(st.session_state.history):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Agent:** {a}")
    st.divider()