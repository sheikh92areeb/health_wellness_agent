from agents import Tool
from typing import List
import asyncio

class MealPlannerTool(Tool):
    name = "MealPlannerTool"
    description = "Suggest 7-day meal plan for user."

    async def call(self, input, context):
        preferences = context.diet_preferences or "balanced"
        meal_plan = [f"Day {i+1}: {preferences} meal" for i in range(7)]
        await asyncio.sleep(0.2)
        context.meal_plan = meal_plan
        return {"meal_plan": meal_plan}