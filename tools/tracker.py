from agents import function_tool
from pydantic import BaseModel

class ProgressUpdate(BaseModel):
    update: str

class TrackerResponse(BaseModel):
    message: str

@function_tool
async def tracker(input: ProgressUpdate, context) -> TrackerResponse:
    context.progress_logs.append({"update": input.update})
    return TrackerResponse(message="Progress saved.")