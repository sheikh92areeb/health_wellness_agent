from pydantic import BaseModel, ValidationError

def validate_goal_input(goal_text: str):
    import re
    pattren = r"(\d+)(Kg|lbs|pounds) in (\d+) (days|weeks|months)"
    return bool(re.search(pattren, goal_text.lower()))

def enforce_output_structure(data, model):
    try:
        return model(**data)
    except ValidationError as e:
        raise ValueError("Invalid Tool output format", e)
    