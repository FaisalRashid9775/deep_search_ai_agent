from agents import function_tool, RunContextWrapper
from dataclasses import dataclass

@dataclass
class userInfo:
    name: str
    city: str
    topic: str

@function_tool()
def userInformation(context: RunContextWrapper[userInfo]):
    """Getting information about user"""
    return f"You’re helping {context.context.name} from {context.context.city} who likes {context.context.topic}. Personalise examples accordingly."
