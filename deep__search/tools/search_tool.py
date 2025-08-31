from agents import function_tool
from config.settings import tavily_client

@function_tool()
def search(query: str):
    print(f"searching for: {query}")
    response = tavily_client.search(query)
    return response
