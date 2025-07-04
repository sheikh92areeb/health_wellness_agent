from openai import RunHooks

class GlobalHooks(RunHooks):
    async def on_tool_start(self, tool_call, context):
        print(f"[Hook] Tool {tool_call.tool.name} started")

    async def on_tool_end(self, tool_call, context):
        print(f"[Hook] Tool {tool_call.tool.name} finished")

    async def on_handoff(self, handoff_call, context):
        context.handoff_logs.append(f"Handoff to {handoff_call.target.name}")
        print(f"[Hook] Handoff to {handoff_call.target.name}")

global_hooks = GlobalHooks()