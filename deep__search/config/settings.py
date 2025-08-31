import os
from dotenv import find_dotenv, load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from tavily import TavilyClient

# Load environment variables
load_dotenv(find_dotenv())

api_key = os.environ.get("GOOGLE_API_KEY")
tavily_api_key = os.environ.get("TAVILY_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# Tavily client
tavily_client = TavilyClient(api_key=tavily_api_key)

# OpenAI Client (Gemini API)
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Models
lite_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)

good_model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=client
)
