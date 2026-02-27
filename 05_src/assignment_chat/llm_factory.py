# llm_factory.py

import os
from openai import OpenAI
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from langchain_openai import ChatOpenAI
from pathlib import Path
from dotenv import load_dotenv

# Load the .secrets file
env_path = Path(__file__).parent.parent / ".secrets"
load_dotenv(dotenv_path=env_path)

# Access your environment variable
api_gateway_key = os.getenv("API_GATEWAY_KEY")

print("api_gateway_key", api_gateway_key[:3])

API_BASE = "https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1"
DEFAULT_HEADERS = { "x-api-key": api_gateway_key }
EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_OPENAI_MODEL = "gpt-4o"

def create_openai_client(
    base_url: str | None = None,
    api_key: str | None = None,
) -> OpenAI:
    """
    Create and return a configured OpenAI client using API_GATEWAY.
    """

    return OpenAI(
        base_url=base_url or API_BASE,
        api_key=api_key or "any",
        default_headers=DEFAULT_HEADERS,
    )


def create_embedding_function() -> OpenAIEmbeddingFunction:
    """
    Create and return a Chroma-compatible OpenAI embedding function using API_GATEWAY.
    """

    ef = OpenAIEmbeddingFunction(
        api_base=API_BASE,
        model_name=EMBEDDING_MODEL,
        api_key="any",
        default_headers=DEFAULT_HEADERS,
    )

    ef._client = create_openai_client()

    return ef

def create_chat_agent(
        base_url: str | None = None,
        model: str | None = None
) -> ChatOpenAI:
    """
    Create and return a configured ChatOpenAI using API_GATEWAY.
    """

    return ChatOpenAI(
        model=model or CHAT_OPENAI_MODEL,
        base_url=base_url or API_BASE,
        default_headers=DEFAULT_HEADERS,
    )
