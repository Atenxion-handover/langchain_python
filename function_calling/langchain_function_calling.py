from langchain_openai import ChatOpenAI
from helpers.config import Config
from langchain_core.tools import tool
from typing import Annotated
from langchain_core.messages import HumanMessage
import requests
from langchain_core.messages import ToolMessage
from langchain_community.callbacks.manager import get_openai_callback
import time


@tool("multiply")
def multiply(
    a: Annotated[int, "First Number"], b: Annotated[int, "Second Number"]
) -> int:
    """Multiply Two Numbers"""
    return a * b


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


# print(multiply.args_schema.schema())
# {
#     "title": "multiplySchema",
#     "description": "Multiply Two Numbers",
#     "type": "object",
#     "properties": {
#         "a": {"title": "A", "description": "First Number", "type": "integer"},
#         "b": {"title": "B", "description": "Second Number", "type": "integer"},
#     },
#     "required": ["a", "b"],
# }


tools = [multiply, get_weather]
llm = ChatOpenAI(model="gpt-4o-mini", api_key=Config.OPENAI_API_KEY)
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=True)
query = "How is the weather in London?"
messages = [HumanMessage(query)]

start_time = time.perf_counter()
with get_openai_callback() as cb:
    result = llm_with_tools.invoke(query)

    if result.tool_calls:
        messages.append(result)

        for tool_call in result.tool_calls:
            selected_tool = next(
                temp_tool for temp_tool in tools if temp_tool.name == tool_call["name"]
            )
            tool_response = selected_tool.invoke(tool_call)
            messages.append(tool_response)
        result = llm_with_tools.invoke(messages)
    else:
        pass

    print(result)
    print(cb)

print(f"{time.perf_counter() - start_time}s")
