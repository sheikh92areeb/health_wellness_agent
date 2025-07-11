from agents import function_tool
from pydantic import BaseModel, ConfigDict
from typing import List

class WorkoutInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

class WorkoutPlan(BaseModel):
    weekly_plan: List[str]
    model_config = ConfigDict(extra="forbid")

@function_tool
async def workout_recommender(input: WorkoutInput, context) -> WorkoutPlan:
    goal_data = context.goal or {}
    goal_text = goal_data.get("goal_text", "").lower()

    if "gain" in goal_text or "muscle" in goal_text:
        plan = ["Strength", "Strength", "Cardio", "Rest", "Strength", "Core", "Stretch"]
    elif "weight" in goal_text or "lose" in goal_text or "fat" in goal_text:
        plan = ["Cardio", "HIIT", "Strength", "Cardio", "Rest", "Yoga", "Walk"]
    elif "fit" in goal_text or "healthy" in goal_text:
        plan = ["Walk", "Yoga", "Cardio", "Stretch", "Rest", "Strength", "Yoga"]
    else:
        # Default beginner-friendly plan
        plan = ["Walk", "Rest", "Cardio", "Yoga", "Stretch", "Walk", "Rest"]
    
    context.workout_plan = {"weekly_plan": plan, "base_on_goal_text": goal_text}
    return WorkoutPlan(weekly_plan=plan)