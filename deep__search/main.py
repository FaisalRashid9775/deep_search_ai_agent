import asyncio
from agents import Runner
from agent.main_agents import main_agent
from tools.user_info_tool import userInfo


async def main():
    userInfo1 = userInfo("Ali", "Islamabad", "He is interested in Business")
    result = await Runner.run(
        main_agent,
        """Which fical color is beter white or black. Give reponse on the basics of opion of people of indo-pak""",
        context=userInfo1
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
