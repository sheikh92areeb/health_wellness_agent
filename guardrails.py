from pydantic import BaseModel, ValidationError

def validate_goal_input(goal_text: str):
    import re
    pattern = r"(\d+)(kg|lbs|pounds) in (\d+) (days|weeks|months)"
    return bool(re.search(pattern, goal_text.lower()))


class StructuredGaol(BaseModel):
    structured_goal: dict
    
def enforce_output_structure(data, model):
    try:
        return model(**data)
    except ValidationError as e:
        raise ValueError("Invalid Tool Output Formate", e)
