# `adaptive_rag.ipynb`

Notebook: `adaptive_rag.ipynb`

## What it does

Builds an “adaptive RAG” chain:

- Classifies incoming queries as **RELATED** (answerable from the Brillar Bank fixed-deposit knowledge base) vs **NOT_RELATED**.
- For RELATED queries, runs a standard RAG pass and then optionally performs up to a few extra retrieval+answer loops to fill missing details.
- For NOT_RELATED queries, skips retrieval and answers directly using the LLM’s general knowledge.

## Workflow (step-by-step)

1. **Load Env**
   - Loads environment variables (API keys, DB credentials) from `.env`.
2. **Get Embeddings**
   - Creates an embedding model (OpenAI embeddings) used for vector search.
3. **Get Retriever**
   - Connects to a Chroma collection (`collection_name="adaptive_rag_test_3"`) and builds a similarity retriever (`k=top_k`).
4. **Define LLM**
   - Creates a chat model for generation (OpenAI chat model).
5. **Create Contextualize Chain**
   - If there is chat history, rewrites the latest user question into a standalone question before retrieval; otherwise uses the raw question.
6. **Define Query Classifier**
   - Defines a structured-output schema (`ClassifierSchema`) and a classifier prompt that labels queries as `RELATED` or `NOT_RELATED`.
   - Uses `langchain_ollama.ChatOllama` in this notebook for classification (local model runtime).
7. **Create QA Chain**
   - Creates a prompt that answers using retrieved context only.
8. **Adaptive Chain**
   - Creates a second structured-output schema (`AdaptiveSchema`) that decides whether the current answer is final, or if another retrieval pass is needed.
9. **Retriever Chain**
   - Wires `question → retriever` to fetch documents for the current query.
10. **QA Loop**
   - Runs an iterative loop:
     - Ask the adaptive controller if the current answer is sufficient.
     - If not, generate a follow-up retrieval query, retrieve again, answer that follow-up, and repeat (up to a small cap).
11. **Create Final Chain (Contextualize → Retrieval → QA → Adaptive)**
   - Uses the classifier to route:
     - `RELATED` → full adaptive RAG chain.
     - `NOT_RELATED` → “external knowledge” chain (LLM-only answer).
12. **Invoke Chain**
   - Executes the end-to-end chain on example questions and prints intermediate/final results.

## Helper usage (high level)

- Uses LangChain “runnables” (`RunnablePassthrough`, `RunnableParallel`, `@chain`) to compose the pipeline.
- Uses Chroma as the vector store; this notebook connects to a named collection and assumes it already contains the Brillar Bank content.

