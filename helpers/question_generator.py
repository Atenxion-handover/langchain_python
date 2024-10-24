from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.language_models import LanguageModelLike
from langchain_core.documents import Document
from typing import List, Tuple


def get_question_generator(
    llm: LanguageModelLike,
    context: List[Document],
    chat_history: List[Tuple[str, str]],
    k: int,
) -> str:
    prompt = """Generate {k} possible follow up questions based on the given chat history and context. You should follow the instructions below.

  - Don't answer the questions.
  - Don't include any introductory text, explanations, or follow-up sentences.
  - Don't number the question list.
  - Keep the questions short and direct. 
  - Only generate contextually answerable questions.
  - List the questions in a single line, separated by commas without whitespaces.

  Example response: What is a cat?,How many legs do they have?
  ---------------------------------------------------
  Chat History: {chat_history}
  Context: {context}
  """
    prompt_template = ChatPromptTemplate.from_template(prompt)

    def get_chat_history(input_):
        return "\n".join([f"{role}: {content}" for role, content in input_])

    def get_context(input_):
        return input_[0].page_content

    generator_chain = (
        {
            "chat_history": itemgetter("chat_history")
            | RunnableLambda(get_chat_history),
            "context": itemgetter("context") | RunnableLambda(get_context),
            "k": itemgetter("k"),
        }
        | prompt_template
        | llm
        | StrOutputParser()
    )
    result = generator_chain.invoke(
        {"chat_history": chat_history, "context": context, "k": k}
    )

    return result
