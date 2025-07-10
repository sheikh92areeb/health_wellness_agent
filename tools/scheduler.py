from agents import function_tool
from pydantic import BaseModel

class CheckinInfo(BaseModel):
    checkin: str

@function_tool
async def scheduler(input:dict, context) -> CheckinInfo:
    return CheckinInfo(checkin="Scheduled weekly every Monday at 9am.")