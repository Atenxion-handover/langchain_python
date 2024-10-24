from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from typing import Annotated
import requests
from helpers import get_llm
from langchain_community.callbacks.manager import get_openai_callback
import time


@tool("get_weather")
def get_weather(
    location: Annotated[str, "Location for the weather forecast, e.g. London, UK"]
):
    """Forecast the weather for the provided location."""
    api_key = "777c42660156447db5842748240110"
    result = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    )

    return result.json()


tools = [get_weather]

llm = get_llm("gpt-4o-mini")
agent = create_react_agent(llm, tools, debug=True)

question = [("human", "How is the weather in London?")]

start_time = time.perf_counter()
with get_openai_callback() as cb:
    agent.invoke({"messages": question})
    print(cb)

print(f"{time.perf_counter() - start_time}s")
