from agents import Agent, ModelSettings
from config.settings import lite_model
from agent.multiple_agent import multiple_agent
from agent.conflict_agent import conflict_agent
from agent.report_agent import report_agent

lead_research_Agent = Agent(
    name="lead_research_Agent",
    instructions=""" Your responsibilities are:

   1. Receive the research plan from the planning_agent.  
   2. For each topic in the plan, call multiple_agent to gather research results.  
   3. Compare and analyze the results.  
      - If you find **inconsistent or contradictory information**, send the findings to conflict_agent for review.  
      - If information is consistent, send it directly to report_agent.  
   4. Once conflict_agent has resolved conflicts (if any), forward the final resolved data to report_agent.  
   5. Ensure the report_agent is the **only agent** responsible for writing the final report.  """,
    model=lite_model,
    model_settings=ModelSettings(max_tokens=200000, temperature=0.5),
    tools=[
        multiple_agent.as_tool("multiple_Agent", "Research on topics"),
        conflict_agent.as_tool("conflict_Agent", "Give response on conflicts"),
        report_agent.as_tool("report_agent", "Give final report")
    ]
)
