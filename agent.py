import os
from dotenv import load_dotenv
from agents import Agent
from handoffs_agents.escalation_agent import escalation_agent 
from handoffs_agents.injury_support_agent import injury_support_agent
from handoffs_agents.nutrition_expert_agent import nutrition_expert_agent
from tools.goal_analyzer import goal_analyzer
from tools.meal_planner import meal_planner
from tools.workout_recommender import workout_recommender
from tools.scheduler import scheduler
from tools.tracker import tracker
from hooks import agent_hooks

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
        tools=[
            goal_analyzer,
            meal_planner,
            workout_recommender,
            scheduler,
            tracker
        ],
        handoffs=[
            escalation_agent,
            injury_support_agent,
            nutrition_expert_agent
        ],
        hooks=agent_hooks,
        model=gemini_model
    )
