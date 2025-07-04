from agent import build_health_wellness_agent
from context import get_user_context
from openai import Runner
import asyncio

def run_cli():
    context = get_user_context()
    agent = build_health_wellness_agent()
    user_input = input("👤 You: ")

    async def main():
        async for step in Runner.stream(agent, user_input, context):
            print("🤖 ", step.pretty_output)

    asyncio.run(main())

if __name__ == "__main__":
    run_cli()