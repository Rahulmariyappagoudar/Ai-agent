from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama

from .tools import retrieval_tool


def get_agent():
    llm = Ollama(model="mistral")

    tools = [retrieval_tool()]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    return agent
