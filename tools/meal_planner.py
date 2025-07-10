import asyncio
from agents import function_tool
from typing import List
from pydantic import BaseModel

class MealPlanOutput(BaseModel):
    meal_plan: List[str]

@function_tool
async def meal_planner(input: dict, context) -> MealPlanOutput:
    preference = context.diet_preferences or "balanced"
    meal_plan = [f"Day {i+1}: {preference} meals" for i in range(7)]
    await asyncio.sleep(0.2)
    context.meal_plan = meal_plan
    return MealPlanOutput(meal_plan=meal_plan)