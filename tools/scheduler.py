from agents import function_tool
from pydantic import BaseModel, ConfigDict

class SchedulerInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

class CheckinInfo(BaseModel):
    checkin: str
    model_config = ConfigDict(extra="forbid")

@function_tool
async def scheduler(input: SchedulerInput, context) -> CheckinInfo:
    return CheckinInfo(checkin="Scheduled weekly every Monday at 9am.")
