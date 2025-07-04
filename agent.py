from agents import Agent
from hooks import global_hooks
from context import UserSessionContext
from tools.goal_analyzer import GoalAnalyzerTool
from tools.meal_planner import MealPlannerTool
from tools.workout_recommender import WorkoutRecommenderTool
from tools.scheduler import CheckinSchedulerTool
from tools.tracker import ProgressTrackerTool
from agents.escalation_agent import esclation_agent
from agents.injury_support_agent import injury_support_agent
from agents.nutrition_expert_agent import nutrition_expert_agent

def build_health_wellness_agent():
    return Agent(
        name="HealthWellnessPlannerAgent",
        instructions="Assist users with fitness, dietary planning, progress tracking, and more.",
        tools=[
            GoalAnalyzerTool(),
            MealPlannerTool(),
            WorkoutRecommenderTool(),
            CheckinSchedulerTool(),
            ProgressTrackerTool()
        ],
        handoffs = {
            "escalation": esclation_agent,
            "injury_support": injury_support_agent,
            "nutrition_expert": nutrition_expert_agent
        },
        hooks=global_hooks,
    )