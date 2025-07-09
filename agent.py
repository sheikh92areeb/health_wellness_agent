import os
from dotenv import load_dotenv
from agents import Agent
from handoffs_agents import escalation_agent, injury_support_agent, nutrition_expert_agent

load_dotenv()
gemini_model = os.getenv("GEMINI_MODEL")

def build_health_welness_agent():
    return Agent(
        name='health_welness_agent',
        instructions=(
            "You are a helpful and supportive Health and Wellness AI Agent. "
            "Assist users in their fitness, diet, mental well-being, and physical routine goals. "
            "Use tools like goal analysis, meal planning, scheduling, and workout recommendations. "
            "Track progress and hand off complex tasks to specialist agents. "
            "Be empathetic, motivational, and avoid giving medical advice."
        ),
        tools=[],
        handoffs=[
            escalation_agent,
            injury_support_agent,
            nutrition_expert_agent
        ],
        model=gemini_model
    )
