import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api('chat_completions')

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)