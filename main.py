import os
import asyncio
from dotenv import load_dotenv
from agents import Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
from agent import build_health_welness_agent
from context import get_user_context
from hooks import run_hooks
from utils.streaming import stream_agent_output

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

set_tracing_disabled(True)
set_default_openai_api('chat_completions')

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_client(external_client)

def run_cli():
    context = get_user_context()
    agent = build_health_welness_agent()

    while True:
        user_input = input("👤 You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("👋 Goodbye! Stay healthy!")
            break

        async def main():
            print("🤖 AI:")
            result = Runner.run_streamed(
                starting_agent=agent,
                input=user_input,
                context=context,
                hooks=run_hooks
            )

            async for chunk in stream_agent_output(result):
                print(chunk, end="", flush=True)
            print("\n")
    
        asyncio.run(main())

if __name__ == "__main__":
    run_cli()