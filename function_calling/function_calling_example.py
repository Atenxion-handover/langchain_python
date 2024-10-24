from operator import itemgetter
from helpers import get_llm, get_retriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnablePassthrough, chain
from langchain.globals import set_debug
from langchain_core.tools import tool
from typing import Annotated
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import requests

# set_debug(True)


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


@tool("get_interest_rate")
def get_interest_rate(
    amount: Annotated[int, "Amount of deposit"],
    interest_rate: Annotated[float, "Interest rate percentage"],
    term: Annotated[int, "Maturity period in month"],
):
    """Interest calculation for fixed deposit."""
    interest = amount * (interest_rate / 100) * (term / 12)
    if term > 36:
        interest += 1111

    return interest


tools = [get_weather, get_interest_rate]

llm = get_llm("gpt-4o-mini")


retriever = get_retriever(
    index_name="test",
    embedding_model="text-embedding-3-large",
    dimension=256,
    vector_db="qdrant",
    top_k=3,
)


contextualize_instructions = """Convert the latest user question into a standalone question given the chat history. Don't answer the question, return the question and nothing else (no descriptive text)."""
contextualize_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_instructions),
        ("placeholder", "{chat_history}"),
        ("human", "{question}"),
    ]
)
contextualize_question = contextualize_prompt | llm | StrOutputParser()

qa_instructions = (
    """Answer the user question given the following context:\n\n{context}."""
)
qa_prompt = ChatPromptTemplate.from_messages(
    [("system", qa_instructions), ("human", "{question}")]
)

# question = "How is the weather today in Yangon?"


@chain
def tool_calling(input_: dict) -> Runnable:
    print(input_)
    if input_.tool_calls:
        test_instruction = """Answer the question using the tool response."""
        test_prompt = ChatPromptTemplate(
            [("system", test_instruction), ("human", "{question}")]
        )
        test_prompt.messages.append(input_)
        for tool_call in input_.tool_calls:
            selected_tool = next(
                temp_tool for temp_tool in tools if temp_tool.name == tool_call["name"]
            )
            tool_response = selected_tool.invoke(tool_call)
            test_prompt.messages.append(tool_response)
        prompt = test_prompt.invoke({"question": question})
        result = llm.invoke(prompt)
        return result
    else:
        return input_


@chain
def contextualize_if_needed(input_: dict) -> Runnable:
    if input_.get("chat_history"):
        return contextualize_question
    else:
        return RunnablePassthrough() | itemgetter("question")


def format_docs(docs):
    return "".join(doc.page_content for doc in docs)


rag_chain_from_docs = (
    {
        "question": itemgetter("question"),  # input query
        "context": lambda x: format_docs(x["context"]),  # context
    }
    | qa_prompt
    | llm.bind_tools(tools)
    | tool_calling
    | StrOutputParser()
)


# Pass input query to retriever
retrieve_docs = itemgetter("question") | retriever

final_chain = (
    RunnablePassthrough.assign(question=contextualize_if_needed)
    .assign(context=retrieve_docs)
    .assign(answer=rag_chain_from_docs)
)

question = "tell me about brillar bank?"

result = final_chain.invoke(
    {
        "question": question,
        "chat_history": [
            # ("human", "do you know the interest rates for fixed deposit?"),
            # ("ai", "Yes"),
        ],
    }
)

print(result)
