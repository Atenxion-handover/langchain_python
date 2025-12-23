# `base_workflow.ipynb`

Notebook: `base_workflow.ipynb`

## What it does

Implements a minimal RAG pipeline on top of a Chroma vector store:

`(optional contextualize) → retrieve docs → answer from context`

This is the “baseline” workflow that other notebooks extend with tracing, reranking, corrective steps, etc.

## Workflow (step-by-step)

1. **Load Env**
   - Loads `.env` variables (API keys and Chroma Cloud credentials).
2. **Get Embeddings**
   - Creates an OpenAI embedding model used by the vector store for similarity search.
3. **Get Retriever**
   - Connects to Chroma (`collection_name="adaptive_rag_test_3"`) and creates a retriever with top-k similarity search.
4. **Define LLM**
   - Instantiates a chat model for generation (OpenAI `ChatOpenAI`).
5. **Create Contextualize Chain**
   - Builds a small chain that rewrites the user’s latest message into a standalone question when chat history exists.
6. **Create QA Chain**
   - Builds a prompt+LLM chain that answers strictly from `{context}`.
7. **Retriever Chain**
   - `question → retriever` produces the retrieved document list.
8. **Create Final Chain (Contextualize → Retrieval → Corrective)**
   - Composes:
     - contextualization (when needed),
     - retrieval,
     - and answering.
9. **Invoke Chain**
   - Runs a few example questions through the pipeline.

## Notes

- This notebook assumes the Chroma collection already contains the Brillar Bank fixed-deposit content.

