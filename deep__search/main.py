import asyncio
from agents import Runner
from agent.main_agents import main_agent
from tools.user_info_tool import userInfo


async def main():
    userInfo1 = userInfo("Ali", "Islamabad", "He is interested in Business")
    result = Runner.run_streamed(
        main_agent,
        """Electric car vs Disel Car. Which is better""",
        context=userInfo1
    )
    async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
