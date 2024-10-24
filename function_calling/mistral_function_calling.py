from mistralai import Mistral
from helpers.config import Config
import functools
import json


MISTRAL_API_KEY = Config.MISTRAL_API_KEY
messages = [{"role": "user", "content": "How is the weather in Yangon?"}]

client = Mistral(api_key=MISTRAL_API_KEY)


def get_weather(location: str) -> str:
    return {"data": f"It is hot in {location}"}


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get Today's Weather in Specified Location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The location for the weather forecast.",
                    }
                },
                "required": ["location"],
            },
        },
    },
]

names_to_functions = {"get_weather": functools.partial(get_weather)}

response = client.chat.complete(
    model="open-mixtral-8x22b", messages=messages, tools=tools
)
tool_call_response = response.choices[0].message
messages.append(tool_call_response)

tool_call = response.choices[0].message.tool_calls[0]
function_name = tool_call.function.name
function_params = json.loads(tool_call.function.arguments)
function_result = names_to_functions[function_name](function_params)
messages.append(
    {
        "role": "tool",
        "name": function_name,
        "content": json.dumps(function_result),
        "tool_call_id": tool_call.id,
    }
)
response = client.chat.complete(model="open-mixtral-8x22b", messages=messages)
print(response)
