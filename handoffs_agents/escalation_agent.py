import os
from dotenv import load_dotenv
from agents import Agent

load_dotenv()
gemini_model = os.getenv("GEMINI_MODEL")

escalation_agent = Agent(
    name="EscalationAgent",
    instructions="Assist as a human trainer when requested.",
    model=gemini_model
)