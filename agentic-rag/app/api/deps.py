# API dependencies
from functools import lru_cache
from app.agents.agent_chain import get_agent


@lru_cache
def get_agent_instance():
    return get_agent()
