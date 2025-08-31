from agents import Agent
from config.settings import good_model

conflict_agent = Agent(
    name="conflict_agent",
    instructions="""You are helpful agent. Get details from lead_research_agent, analyze, and send your response to report_agent.""",
    model=good_model
)
