# `notebooks/sparse_bm25.ipynb`

Notebook: `notebooks/sparse_bm25.ipynb`

## What it does

Builds a custom Elasticsearch retriever that combines:

- BM25 lexical match (`match` query)
- ELSER sparse semantic match (`text_expansion`)

…then fuses rankings using **RRF (reciprocal rank fusion)** and runs a conversational retrieval chain on the fused results.

## Workflow (step-by-step)

1. **Load API Keys**
   - Loads `.env` variables for Elasticsearch and the LLM.
2. **Load Contents from Brillar Bank**
   - Crawls pages into documents.
3. **Split the Loaded Data into Chunks**
   - Splits for indexing.
4. **Get Embedding Model**
   - (Not required for ELSER/BM25 fusion itself, but may be part of shared setup.)
5. **Instantiate Elasticsearch Store**
   - Indexes documents into a sparse index using `SparseVectorStrategy(model_id=".elser_model_2")` (`index_name="bm25_sparse"`).
6. **Get LLM**
   - Instantiates the answer model.
7. **Get Retriever**
   - Defines a custom `hybrid_query(...)` with `sub_searches` and `rrf` ranking.
   - Creates an `ElasticsearchRetriever.from_es_params(...)` that uses that query builder.
8. **Create Chain**
   - Creates a conversational retrieval chain.
9. **Invoke Chain**
   - Runs sample questions.

## Notes

- Requires `ELASTIC_CLOUD_ID` and `ELASTIC_API_KEY`.
- Requires the ELSER model to be available in your Elasticsearch cluster.

