# `notebooks/just_bm25.ipynb`

Notebook: `notebooks/just_bm25.ipynb`

## What it does

Creates a BM25-only Elasticsearch index from Brillar Bank content, then runs a conversational retrieval chain on lexical search results.

This notebook is meant to be a “BM25 only” baseline for comparing against dense/sparse/hybrid variants.

## Workflow (step-by-step)

1. **Load API Keys**
   - Loads `.env` variables (Elasticsearch + LLM keys).
2. **Load Contents from Brillar Bank**
   - Fetches/crawls web content into documents.
3. **Split the Loaded Data into Chunks**
   - Splits documents for indexing.
4. **Get Embedding Model**
   - (May still create embeddings in shared scaffolding, but BM25 retrieval itself is lexical.)
5. **Instantiate Elasticsearch Store**
   - Indexes documents using `BM25Strategy()` (`index_name="just_bm25"`).
6. **Get LLM**
   - Instantiates the answer model.
7. **Get Retriever**
   - Creates a BM25 retriever from the store.
8. **Create Chain**
   - Uses `helpers.conversation_retrieval_chain.create_conversational_retrieval_chain(...)`.
9. **Invoke Chain**
   - Runs sample questions.

## Notes

- Requires `ELASTIC_CLOUD_ID` and `ELASTIC_API_KEY`.

