# `source_tuning/related_sources.ipynb`

Notebook: `source_tuning/related_sources.ipynb`

## What it does

Runs a RAG + tool-calling workflow similar to `function_calling/function_calling_and_question_generation.ipynb`, then performs an extra “source attribution” pass:

- Given the model’s answer and the retrieved documents, ask the LLM to infer which document sources the answer most likely came from.

## Workflow (step-by-step)

1. **Import Necessary Modules**
   - Imports LangChain runnables and helper entry points.
2. **Define Functions and Schema**
   - Defines tool functions and schemas using `@tool`.
3. **Create Tool Collection**
   - Collects tools and binds them to the LLM.
4. **Initiate Retriever**
   - Creates a retriever via `helpers.get_retriever(...)`.
5. **Initiate LLM**
   - Creates a chat model via `helpers.get_llm(...)` and binds tools.
6. **Create Instructions for RAG Chain**
   - Defines prompts for contextualization + QA.
7. **Create a RAG Chain Combined with Tool Calling**
   - Executes tool calls when present and re-invokes the LLM with tool outputs.
8. **Invoke the Chain**
   - Runs sample questions through the combined chain.

## Notes

- The “Get Sources” step is a best-effort heuristic (it asks an LLM to infer provenance from passages + answer).
