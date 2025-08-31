from agents import Agent, ModelSettings
from config.settings import lite_model
from tools.user_info_tool import userInformation
from agent.planning_agent import planning_Agent

main_agent = Agent(
    name="main_agent",
    instructions="""You are deep research agent. Flow:
    1. Call userInformation tool for user-specific context.
    2. Send response to planning agent.
    3. Planning agent → lead_research_agent → conflict_agent/report_agent chain.
    4. Final report must be delivered by report_agent.""",
    model=lite_model,
    model_settings=ModelSettings(max_tokens=200000, temperature=0.5),
    tools=[userInformation],
    handoffs=[planning_Agent]
)
