from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.recommender import RecommendationAgent
from agents.critic import CriticAgent

from core.fake_llm import FakeLLM

from tools.registry import ToolRegistry
from tools.fetch_data import FetchData
from tools.analyze_data import AnalyzeData


def main():
    # -----------------------------
    # LLM (Deterministic / Offline)
    # -----------------------------
    llm = FakeLLM()

    # -----------------------------
    # Planner
    # -----------------------------
    planner = PlannerAgent(llm)

    # -----------------------------
    # Tool Registry
    # -----------------------------
    registry = ToolRegistry()
    registry.register(FetchData())
    registry.register(AnalyzeData())

    # -----------------------------
    # Executor
    # -----------------------------
    executor = ExecutorAgent(registry)

    # -----------------------------
    # Recommendation & Critic Agents
    # -----------------------------
    recommender = RecommendationAgent(llm)
    critic = CriticAgent()

    # -----------------------------
    # Run pipeline
    # -----------------------------
    plan = planner.plan(
        "Analyze my campaign performance and suggest improvements"
    )

    print("\n=== PLAN ===")
    print(plan)

    execution_result = executor.execute(plan)

    print("\n=== EXECUTION RESULT ===")
    print(execution_result)

    recommendations = recommender.recommend(execution_result)

    print("\n=== RECOMMENDATIONS ===")
    for r in recommendations.recommendations:
        print(f"- {r.recommendation} ({r.confidence})")
        print(f"  Reason: {r.reason}")

    # -----------------------------
    # Critic Review
    # -----------------------------
    critic_result = critic.evaluate(recommendations)

    print("\n=== CRITIC REVIEW ===")
    for f in critic_result.feedback:
        print(f"- {f.recommendation}")
        print(f"  Verdict: {f.verdict}")
        print(f"  Confidence: {f.confidence}")
        print(f"  Reason: {f.reason}")


if __name__ == "__main__":
    main()
