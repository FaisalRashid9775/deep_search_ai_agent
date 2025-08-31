from agents import Agent
from config.settings import good_model

report_agent = Agent(
    name="report_agent",
    instructions="""You are helpful report writing agent. You have 3 responsibilities:
    1. Get content from multiple_agent if available 
    2. Get content from conflict_agent if available 
    3. Make a report based on both agents.  
    If no data, respond with 'I am sorry I did not get any data
    Report should be professional. Before starting report place today date.""",
    model=good_model
)
