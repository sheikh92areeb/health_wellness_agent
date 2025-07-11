import asyncio
import config
from agents import Runner
from agent import build_health_welness_agent
from context import get_user_context
from hooks import run_hooks
from utils.streaming import stream_agent_output



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