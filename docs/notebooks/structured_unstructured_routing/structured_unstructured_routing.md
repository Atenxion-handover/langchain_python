# `structured_unstructured_routing/structured_unstructured_routing.ipynb`

Notebook: `structured_unstructured_routing/structured_unstructured_routing.ipynb`

## What it does

Demonstrates routing a question to one of two answer paths:

- **Structured path (SQL):** Generate and execute a SQL query against a Postgres database, then answer from the SQL results.
- **Unstructured path (RAG):** Retrieve documents from a vector store, then answer from retrieved context.

It builds two router variants:

- **LLM router:** classify the question with an LLM into SQL vs RAG.
- **Embedding router:** retrieve a “routing document” from a vector store and route based on its metadata.

## Workflow (step-by-step)

1. **Configure Database**
   - Creates a SQLAlchemy engine using `Config.POSTGRES_CONNECTION_STRING`.
2. **Ingest Data**
   - Loads `./sample_data/brillar_bank_fixed_deposit.xlsx`.
   - Writes each sheet into Postgres (one table per sheet).
   - Inserts a small “routing document” into a Qdrant vector store to support the embedding router.
3. **Initiate LLM**
   - Creates the chat model via `helpers.get_llm(...)`.
4. **Invoke the Chain**
   - Builds and runs:
     - `sql_chain_with_llm_router(...)`
     - `sql_chain_with_embedding_router(...)`
   - Each chain:
     - contextualizes question (if chat history exists),
     - routes the question,
     - executes SQL or retrieval,
     - and generates a final natural-language answer.

## Notes

- Requires `POSTGRES_CONNECTION_STRING` and Qdrant connectivity (via helper configuration).
- The “embedding router” depends on having routing documents with consistent metadata in the vector store.

