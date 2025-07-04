from openai import Agent

nutrition_expert_agent = Agent(
    name="NutritionExpertAgent",
    instruction="Handle complex dietary requests like diabetes allergies.",
)