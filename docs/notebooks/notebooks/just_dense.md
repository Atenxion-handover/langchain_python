# `notebooks/just_dense.ipynb`

Notebook: `notebooks/just_dense.ipynb`

## What it does

Creates a dense-vector-only Elasticsearch index from the Brillar Bank website content, then runs a conversational retrieval chain on it.

This notebook is meant to be a “dense only” baseline for comparing against sparse/BM25/hybrid variants.

## Workflow (step-by-step)

1. **Load API Keys**
   - Loads `.env` variables (OpenAI + Elasticsearch).
2. **Load Contents from Brillar Bank**
   - Uses helper utilities to fetch/crawl Brillar Bank pages into documents.
3. **Split the Loaded Data into Chunks**
   - Splits the documents into smaller chunks for indexing.
4. **Get Embedding Model**
   - Creates an embedding model for dense vector indexing/search.
5. **Instantiate Elasticsearch Store**
   - Indexes documents into Elasticsearch using `DenseVectorStrategy()` (`index_name="just_dense_vector"`).
6. **Get LLM**
   - Instantiates a chat model for answering.
7. **Get Retriever**
   - Creates a dense retriever from the vector store.
8. **Create Chain**
   - Uses `helpers.conversation_retrieval_chain.create_conversational_retrieval_chain(...)` to build a history-aware retrieval QA chain.
9. **Invoke Chain**
   - Runs example questions (often sourced from `helpers.test_data.get_questions()`).

## Notes

- Requires `ELASTIC_CLOUD_ID`, `ELASTIC_API_KEY`, and `OPENAI_API_KEY`.
- Index creation happens inside the notebook via `ElasticsearchStore.from_documents(...)`.

