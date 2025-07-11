from pydantic import BaseModel, ValidationError, ConfigDict

def validate_goal_input(goal_text: str):
    import re
    pattern = r"(\d+)(kg|lbs|pounds) in (\d+) (days|weeks|months)"
    return bool(re.search(pattern, goal_text.lower()))

class StructuredGoal(BaseModel):
    structured_goal: dict
    model_config = ConfigDict(extra="forbid")
    
def enforce_output_structure(data, model):
    try:
        return model(**data)
    except ValidationError as e:
        raise ValueError("Invalid Tool Output Formate", e)
