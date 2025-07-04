from openai import Tool

class WorkoutRecommenderTool(Tool):
    name = "WorkoutRecommenderTool"
    description = "Suggest workout plans based on user fitness goals."

    async def call(self, input, context):
        goal = context.goal or {}
        workout_plan = {"weekly_plan": ["Strength", "Cardio", "Rest", "Stretch"] * 2}
        context.workout_plan = workout_plan
        return {"workout_plan": workout_plan}