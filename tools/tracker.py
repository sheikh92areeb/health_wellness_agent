from openai import Tool

class ProgressTrackerTool(Tool):
    name = "ProgressTrackerTool"
    description = "Tracks and logs progress updates."

    async def call(self, input, context):
        context.progress_logs.append({"update": input})
        return {"message": "Progress saved."}