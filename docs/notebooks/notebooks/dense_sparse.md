# `notebooks/dense_sparse.ipynb`

Notebook: `notebooks/dense_sparse.ipynb`

## What it does

Creates two separate Elasticsearch indices for the same content:

- a **dense** index (`DenseVectorStrategy()`)
- a **sparse** ELSER index (`SparseVectorStrategy(model_id=".elser_model_2")`)

Then queries both and merges results using an `EnsembleRetriever`.

## Workflow (step-by-step)

1. **Load API Keys**
   - Loads `.env` variables (OpenAI + Elasticsearch).
2. **Load Contents from Brillar Bank**
   - Crawls pages into documents.
3. **Split the Loaded Data into Chunks**
   - Splits docs for indexing.
4. **Get Embedding Model**
   - Creates embeddings for the dense index.
5. **Instantiate Elasticsearch Store**
   - Writes documents to:
     - `index_name="dense_vector"` with `DenseVectorStrategy()`
     - `index_name="sparse_vector"` with `SparseVectorStrategy(model_id=".elser_model_2")`
6. **Get LLM**
   - Instantiates the answer model.
7. **Get Retriever**
   - Builds `dense_retriever` and `sparse_retriever`, then combines them with `EnsembleRetriever(...)`.
8. **Create Chain**
   - Creates a conversational retrieval chain over the ensemble retriever.
9. **Invoke Chain**
   - Runs sample queries and prints answers.

## Notes

- Requires `ELASTIC_CLOUD_ID`, `ELASTIC_API_KEY`, and `OPENAI_API_KEY`.
- Requires the ELSER model to be available in your Elasticsearch cluster.

