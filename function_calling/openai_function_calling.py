from openai import OpenAI
from helpers.config import Config
import json


def get_weather(location: str) -> str:
    return {"data": f"It is hot in {location}"}


client = OpenAI(api_key=Config.OPENAI_API_KEY)

messages = []
messages.append(
    {
        "role": "system",
        "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.",
    }
)
messages.append({"role": "user", "content": "How is the weather in Yangon?"})

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                },
                "required": ["location"],
            },
        },
    },
]
response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages, tools=tools
)
tool_response = response.choices[0].message
messages.append(tool_response)

tool_calls = tool_response.tool_calls
if tool_calls:
    tool_call_id = tool_calls[0].id
    function_name = tool_calls[0].function.name
    function_args = json.loads(tool_calls[0].function.arguments)
    if function_name == "get_weather":
        result = get_weather(**function_args)
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call_id,
                "name": function_name,
                "content": result["data"],
            }
        )

response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)

print("Final Response: ", response)
