from agents import function_tool
from pydantic import BaseModel, ConfigDict

class ProgressUpdate(BaseModel):
    update: str
    model_config = ConfigDict(extra="forbid")

class TrackerResponse(BaseModel):
    message: str
    model_config = ConfigDict(extra="forbid")
    
@function_tool
async def tracker(input: ProgressUpdate, context) -> TrackerResponse:
    context.progress_logs.append({"update": input.update})
    return TrackerResponse(message="Progress saved.")