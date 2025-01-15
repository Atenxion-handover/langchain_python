from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import Literal


Models = Literal[
    "chatgpt-4o-latest",
    "gpt-4o-mini",
    "claude-3-5-sonnet-latest",
    "claude-3-5-haiku-latest",
    "gpt-4o-2024-11-20",
    "gpt-4o",
]
Vendors = Literal["openai", "anthropic", "googlegenai", "huggingface", "mistral"]

llm_vendors = {
    "chatgpt-4o-latest": "openai",
    "gpt-4o-2024-11-20": "openai",
    "gpt-4o-mini": "openai",
    "gpt-4o": "openai",
    "gpt-3.5-turbo": "openai",
    "gpt-4-turbo": "openai",
    "claude-3-5-sonnet-latest": "anthropic",
    "claude-3-5-haiku-latest": "anthropic",
    "gemini-2.0-flash-exp": "googlegenai",
    "gemini-1.5-pro": "googlegenai",
    "mistralai/Mixtral-8x7B-Instruct-v0.1": "huggingface",
    "meta-llama/Llama-2-7b-chat-hf": "huggingface",
    "meta-llama/Llama-2-13b-chat-hf": "huggingface",
    "meta-llama/Llama-2-70b-chat-hf": "huggingface",
    "meta-llama/Meta-Llama-3-8B-Instruct": "huggingface",
    "meta-llama/Meta-Llama-3-70B-Instruct": "huggingface",
    "open-mixtral-8x22b": "mistral",
}


def get_llm(
    model: Models, temperature: float = 0.6, top_p: float = 0.9
) -> ChatAnthropic | ChatOpenAI:
    vendor: Vendors = llm_vendors.get(model, "gpt-4o-mini")
    match vendor:
        case "openai":
            return ChatOpenAI(
                model=model, temperature=temperature, top_p=top_p, stream_usage=True
            )
        case "anthropic":
            return ChatAnthropic(
                model=model, temperature=temperature, top_p=top_p, stream_usage=True
            )
        case "googlegenai":
            return ChatGoogleGenerativeAI(
                model=model, temperature=temperature, top_p=top_p
            )
        case "mistral":
            return ChatMistralAI(model=model, temperature=temperature, top_p=top_p)
        case "huggingface":
            base_model = HuggingFaceEndpoint(
                repo_id=model,
                temperature=temperature,
                top_p=top_p,
            )
            return ChatHuggingFace(llm=base_model)
        case _:
            print("LLM Error")
            return
