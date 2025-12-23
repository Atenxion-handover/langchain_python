# `notebooks/just_sparse.ipynb`

Notebook: `notebooks/just_sparse.ipynb`

## What it does

Creates a sparse-only Elasticsearch index from Brillar Bank content using **ELSER** (`text_expansion`), then runs a conversational retrieval chain over it.

This notebook is meant to be a “sparse only” baseline for comparing against dense/BM25/hybrid variants.

## Workflow (step-by-step)

1. **Load API Keys**
   - Loads `.env` variables (Elasticsearch, plus whatever the LLM needs).
2. **Load Contents from Brillar Bank**
   - Crawls Brillar Bank pages into documents (helper-driven).
3. **Split the Loaded Data into Chunks**
   - Splits documents for indexing.
4. **Instantiate Elasticsearch Store**
   - Indexes documents using `SparseVectorStrategy(model_id=".elser_model_2")` (`index_name="brillar_bank"`).
5. **Get LLM**
   - Instantiates the chat model (via helpers).
6. **Get Retriever**
   - Builds a retriever on the sparse index.
7. **Create Chain**
   - Builds a conversational retrieval chain (history-aware question rewriting + retrieval + answer).
8. **Invoke Chain**
   - Runs sample questions.

## Notes

- Requires `ELASTIC_CLOUD_ID` and `ELASTIC_API_KEY`.
- Requires the ELSER model to be available in your Elasticsearch cluster.

