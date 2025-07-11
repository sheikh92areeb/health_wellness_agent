from agents import function_tool
from typing import List
from pydantic import BaseModel, ConfigDict

class MealPlanInput(BaseModel):
    # If you have no inputs, leave it empty — still required
    model_config = ConfigDict(extra="forbid")

class MealPlanOutput(BaseModel):
    meal_plan: List[str]
    model_config = ConfigDict(extra="forbid")

@function_tool
async def meal_planner(input: MealPlanInput, context) -> MealPlanOutput:
    preference = context.diet_preferences or "balanced"
    meals = [f"Day {i+1}: {preference} meal" for i in range(7)]
    context.meal_plan = meals
    return MealPlanOutput(meal_plan=meals)