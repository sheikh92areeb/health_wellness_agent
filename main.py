import os
import asyncio
from dotenv import load_dotenv
from agents import Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
from agent import build_health_welness_agent
from openai.types.responses import ResponseTextDeltaEvent

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api('chat_completions')

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

async def main():
    
    agent = build_health_welness_agent()

    result = Runner.run_streamed(
        agent,
        "I have injury in my hand?"
    )

    async for event in result.stream_events():
        if event.type == 'raw_response_event' and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

    print(result)

if __name__ == "__main__":
    asyncio.run(main())