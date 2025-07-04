from openai import Tool

class CheckinSchedulerTool(Tool):
    name = "CheckinSchedulerTool"
    description = "Schedules weekly check-ins with user."

    async def call(self, input, context):
        return {"checkin": "Scheduled weekly every Monday at 9am."}        