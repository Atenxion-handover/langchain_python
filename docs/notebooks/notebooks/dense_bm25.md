# `notebooks/dense_bm25.ipynb`

Notebook: `notebooks/dense_bm25.ipynb`

## What it does

Indexes Brillar Bank content into an Elasticsearch dense-vector index with **hybrid mode enabled** (dense+BM25), then runs a conversational retrieval chain.

This notebook is intended to compare “hybrid dense+BM25” against other retrieval strategies.

## Workflow (step-by-step)

1. **Load API Keys**
   - Loads `.env` variables (OpenAI + Elasticsearch).
2. **Load Contents from Brillar Bank**
   - Crawls the Brillar Bank pages into documents.
3. **Split the Loaded Data into Chunks**
   - Splits documents for indexing.
4. **Get Embedding Model**
   - Creates a dense embedding model.
5. **Instantiate Elasticsearch Store**
   - Indexes documents with `DenseVectorStrategy(hybrid=True)` (`index_name="hybrid_search1"`).
6. **Get LLM**
   - Instantiates the answer model.
7. **Get Retriever**
   - Builds a retriever from the hybrid store.
8. **Create Chain**
   - Creates a conversational retrieval chain (history-aware retrieval + answer).
9. **Invoke Chain**
   - Runs example queries and prints answers + (optionally) sources.

## Notes

- Requires `ELASTIC_CLOUD_ID`, `ELASTIC_API_KEY`, and `OPENAI_API_KEY`.
