from agents import Agent
from config.settings import lite_model
from tools.search_tool import search

multiple_agent = Agent(
    name="multi_agent",
    instructions="You are helpful agent. Use your search tool and research the topic list briefly.",
    model=lite_model,
    tools=[search]
)
