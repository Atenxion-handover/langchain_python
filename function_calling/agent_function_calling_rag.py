from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langchain_core.runnables import Runnable, RunnablePassthrough, chain
from typing import Annotated
import requests
from helpers import get_llm, get_retriever
from langchain_community.callbacks.manager import get_openai_callback
import time
from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = get_llm("gpt-4o-mini")


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


contextualize_instructions = """Convert the latest user question into a standalone question given the chat history. Don't answer the question, return the question and nothing else (no descriptive text)."""
contextualize_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_instructions),
        ("placeholder", "{chat_history}"),
        ("human", "{question}"),
    ]
)
contextualize_question = contextualize_prompt | llm | StrOutputParser()

qa_instructions = """Answer the user question in the styel of {answer_style} using the following context:\n\n{context}."""
qa_prompt = ChatPromptTemplate.from_messages(
    [("system", qa_instructions), ("human", "{question}")]
)


@chain
def contextualize_if_needed(input_: dict) -> Runnable:
    if input_.get("chat_history"):
        return contextualize_question
    else:
        return RunnablePassthrough() | itemgetter("question")


def format_docs(docs):
    return "".join(doc.page_content for doc in docs)


retriever = get_retriever(
    index_name="test",
    embedding_model="text-embedding-3-large",
    dimension=256,
    vector_db="qdrant",
    top_k=1,
)

rag_chain_from_docs = (
    {
        "question": itemgetter("question"),  # input query
        "context": lambda x: format_docs(x["context"]),  # context
        "answer_style": itemgetter("answer_style"),
    }
    | qa_prompt
    | llm
    | StrOutputParser()
)

retrieve_docs = itemgetter("question") | retriever

final_chain = (
    RunnablePassthrough.assign(question=contextualize_if_needed)
    .assign(context=retrieve_docs)
    .assign(answer=rag_chain_from_docs)
)

rag_tool = final_chain.as_tool(
    name="fixed_deposit",
    description="Get information about fixed deposit",
)
tools = [get_weather, rag_tool]

agent = create_react_agent(llm, tools, debug=True)

question = [("human", "What is brillar bank fixed deposit?")]

start_time = time.perf_counter()
with get_openai_callback() as cb:
    agent.invoke({"messages": question})
    print(cb)

print(f"{time.perf_counter() - start_time}s")
