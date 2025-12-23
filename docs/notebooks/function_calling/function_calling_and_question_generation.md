# `function_calling/function_calling_and_question_generation.ipynb`

Notebook: `function_calling/function_calling_and_question_generation.ipynb`

## What it does

Combines three ideas into one runnable workflow:

1. A RAG pipeline over a vector store.
2. Tool calling (the model can call small “utility” tools during answering).
3. Follow-up question generation based on the retrieved context + chat history.

## Workflow (step-by-step)

1. **Import Necessary Modules**
   - Imports LangChain runnables and helper entry points like `helpers.get_llm` and `helpers.get_retriever`.
2. **Define Functions and Schema**
   - Defines tool functions (e.g., `get_weather`, `get_interest_rate`) using `@tool(...)`.
3. **Create Tool Collection**
   - Collects tool functions into a list and binds them to the LLM.
4. **Initiate Retriever**
   - Creates a vector-store retriever via `helpers.get_retriever(...)` (index + embedding config).
5. **Initiate LLM**
   - Creates a chat model via `helpers.get_llm(...)`, then binds tools (`llm.bind_tools(tools)`).
6. **Create Instructions for RAG Chain**
   - Creates:
     - a “contextualize question” prompt (standalone question from chat history),
     - and a QA prompt that includes `{context}`.
7. **Create a RAG Chain Combined with Tool Calling**
   - Runs the QA prompt through the tool-enabled LLM.
   - If the LLM emits tool calls, executes them and re-invokes the LLM using the tool responses.
8. **Invoke the Chain**
   - Runs example questions and returns the final answer (with tool usage if needed).
9. **Generate Potential Questions**
   - Uses the retrieved context + chat history to generate likely follow-up questions (question generator pattern).

## Notes

- This notebook makes an external HTTP call inside `get_weather` (to a public weather API); you’ll need network access when running it.

