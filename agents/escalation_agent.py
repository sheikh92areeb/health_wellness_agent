from openai import Agent

esclation_agent = Agent(
    name = "EscalationAgent",
    instruction = "Assits as a Human trainer when requested",
)