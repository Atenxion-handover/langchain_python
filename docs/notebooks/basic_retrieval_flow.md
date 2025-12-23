# `basic_retrieval_flow.ipynb`

Notebook: `basic_retrieval_flow.ipynb`

## What it does

Runs a standard conversational RAG workflow on Chroma, with extra instrumentation:

- Extracts token usage via a callback handler.
- Optionally traces calls to Langfuse.

## Workflow (step-by-step)

1. **Load Env**
   - Loads `.env` variables (OpenAI, Chroma, Langfuse, etc.).
2. **Get Embeddings**
   - Uses OpenAI embeddings (fixed dimensions) for vector similarity.
3. **Get Retriever**
   - Connects to Chroma (`collection_name="test"`) and configures a top-k retriever.
4. **Define LLM**
   - Uses `helpers.llm_integrations.get_llm(...)` to instantiate the chat model.
5. **Create Contextualize Chain**
   - Rewrites the user question into a standalone query when chat history exists.
6. **Create Retrieval Chain**
   - Fetches documents from the vector store based on the (possibly contextualized) question.
7. **Create QA Chain**
   - Formats the retrieved documents into a `{context}` string and runs the answer prompt.
8. **Token Usage Callback**
   - Attaches a callback handler to capture prompt/completion/total tokens.
9. **Langfuse Callback**
   - Attaches Langfuse tracing callbacks when enabled and credentials are present.
10. **Create Final Chain (Contextualize → Retrieval → Q&A)**
   - Composes the overall runnable graph and returns answer + retrieved context + metadata.
11. **Invoke Chain**
   - Executes the chain on sample questions and prints results.

## Helper usage (high level)

- `helpers.llm_integrations.get_llm` centralizes chat-model creation.

