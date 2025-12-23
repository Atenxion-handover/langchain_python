# `crag.ipynb`

Notebook: `crag.ipynb`

## What it does

Implements a “Corrective RAG” (CRAG) workflow:

- Retrieve documents from a Chroma vector store.
- Grade whether the retrieved context is relevant.
- If context is only partially relevant (or irrelevant), improve the query and do web search.
- Refine context into smaller “strips” and answer from the refined/combined context.

## Workflow (step-by-step)

1. **Load Env**
   - Loads `.env` variables (OpenAI, Chroma, and web-search credentials).
2. **Get Embeddings**
   - Creates the embedding model used for similarity retrieval.
3. **Get Retriever**
   - Connects to a Chroma collection (`collection_name="crag_test_3"`) and creates a top-k similarity retriever.
4. **Define LLM**
   - Creates an OpenAI chat model for generation.
5. **Create Contextualize Chain**
   - Optional question rewriting when chat history exists.
6. **Create Retrieval Evaluator Chain**
   - Uses structured output (`GraderSchema`) to label retrieval relevance as `high`, `partial`, or `irrelevant`.
7. **Create Query Rephrase Chain for Web Search**
   - Rewrites the question into a web-search-optimized query when retrieval needs help.
8. **Create Knowledge Refinement Chain**
   - Splits retrieved documents into smaller chunks (“strips”) and uses a structured-output model to keep only strips that directly help answer the query.
9. **Create QA Chain**
   - Answers using the finalized context only.
10. **Retriever Chain**
   - Wires `question → retriever`.
11. **Web Search Tool**
   - Uses `TavilySearchResults` to fetch web snippets and convert them into `Document` objects.
12. **Create a Corrective Chain**
   - Control logic based on the relevance grade:
     - `high` → answer from refined internal context.
     - `partial` → combine refined internal context + web results.
     - `irrelevant` → replace context with web results.
13. **Create Final Chain (Contextualize → Retrieval → Corrective)**
   - Composes contextualization, retrieval, correction, and answering into one runnable.
14. **Invoke Chain**
   - Runs example queries and prints relevance decisions + final answers.

## Notes

- Requires `TAVILY_API_KEY` for the web-search tool.
- This notebook assumes the Chroma collection has already been populated with relevant documents for the “internal” retrieval step.

