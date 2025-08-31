from agents import Agent, ModelSettings
from config.settings import lite_model
from agent.lead_research_agent import lead_research_Agent


planning_Agent = Agent(
    name="planning_agent",
    instructions="""You are a helpful planning agent. Responsibilities:
    1. Break down user query in 3 parts.
    2. Make a plan of these.
    3. Send plan to lead_research_agent for processing.""",
    model=lite_model,
    model_settings=ModelSettings(max_tokens=200000, temperature=0.5),
    handoffs=[lead_research_Agent]
)
