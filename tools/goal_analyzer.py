from openai import Tool
from pydantic import BaseModel
from guardrails import validate_goal_input

class GoalInput(BaseModel):
    goal: str

class GoalAnalyzerTool(Tool):
    name = "GoalAnalyzerTool"
    description = "Analyze user goals and extract structured goal info."

    async def call(self, input: GoalInput, context):
        if not validate_goal_input(input.goal):
            raise ValueError("Goal Format is invalid. Use format: 'I want to lose 5Kg in 2 weeks'.")

        context.goal = {"goal_text": input.goal}
        return {"structured_goal": context.goal}
    