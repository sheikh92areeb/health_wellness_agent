from typing import AsyncGenerator

# ✅ For CLI or frontend streaming
def stream_response(response_iter):
    """Yield tokens from a non-async streaming response iterator (fallback)."""
    for token in response_iter:
        yield token

# ✅ Async generator for OpenAI Agent streaming events
async def stream_agent_output(result) -> AsyncGenerator[str, None]:
    async for event in result.stream_events():
        print("EVENT:", event) 
        if hasattr(event, "pretty_output") and event.pretty_output:
            print("YIELDING:", event.pretty_output)
            yield event.pretty_output