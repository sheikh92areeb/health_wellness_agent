import os
from dotenv import load_dotenv
from agents import Agent

load_dotenv()
gemini_model = os.getenv("GEMINI_MODEL")

nutrition_expert_agent = Agent(
    name="NutritionExpertAgent",
    instructions="Handle complex dietary requests like diabetes, allergies.",
    model=gemini_model
)