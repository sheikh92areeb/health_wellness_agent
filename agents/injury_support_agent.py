from openai import Agent

injury_support_agent = Agent(
    name="InjurySupportAgent",
    instruction="Provide support for Users with injuries.",
)