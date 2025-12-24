from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from core.fake_llm import FakeLLM
from tools.registry import ToolRegistry
from tools.fetch_data import FetchData
from tools.analyze_data import AnalyzeData
from tools.generate_recommendations import GenerateRecommendations

if __name__ == "__main__":
    planner = PlannerAgent(FakeLLM())

    registry = ToolRegistry()
    registry.register(FetchData())
    registry.register(AnalyzeData())
    registry.register(GenerateRecommendations())

    executor = ExecutorAgent(registry)

    plan = planner.plan(
        "Analyze my campaign performance and suggest improvements"
    )

    print("\n=== PLAN ===")
    print(plan)

    result = executor.execute(plan)

    print("\n=== EXECUTION RESULT ===")
    print(result)
