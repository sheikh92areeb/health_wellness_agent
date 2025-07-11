from agents import function_tool
from pydantic import BaseModel, ConfigDict
from guardrails import validate_goal_input, enforce_output_structure, StructuredGoal

class GoalInput(BaseModel):
    goal: str
    model_config = ConfigDict(extra="forbid")

@function_tool
async def goal_analyzer(input: GoalInput, context) -> StructuredGoal:
    if not validate_goal_input(input.goal):
        raise ValueError("Goal Format is invalid. Use formate like 'loose 5kg in 2 months'.")

    context.goal = {"goal_text": input.goal}
    result = {"structured_goal": context.goal}
    return enforce_output_structure(result, StructuredGoal)

