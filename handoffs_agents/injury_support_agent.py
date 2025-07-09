import os
from dotenv import load_dotenv
from agents import Agent

load_dotenv()
gemini_model = os.getenv("GEMINI_MODEL")

injury_support_agent = Agent(
    name="InjurySupportAgent",
    instructions="Provide support for users with injuries.",
    model=gemini_model
)