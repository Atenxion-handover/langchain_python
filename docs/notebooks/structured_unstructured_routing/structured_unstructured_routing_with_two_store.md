# `structured_unstructured_routing/structured_unstructured_routing_with_two_store.ipynb`

Notebook: `structured_unstructured_routing/structured_unstructured_routing_with_two_store.ipynb`

## What it does

Extends the structured/unstructured routing idea by introducing a third variant that uses “two stores”:

- one store/approach for routing and/or unstructured retrieval,
- and the Postgres DB for structured querying.

The notebook still demonstrates LLM-based routing and embedding-based routing as well.

## Workflow (step-by-step)

1. **Configure Database**
   - Creates a SQLAlchemy engine for Postgres (`Config.POSTGRES_CONNECTION_STRING`).
2. **Ingest Data**
   - Loads `./sample_data/brillar_bank_fixed_deposit.xlsx`.
   - Writes each sheet into Postgres tables.
   - Loads the same Excel into `Document` objects (via `helpers.load_excel`) and stores them in Qdrant (`index_name="csv_data"`).
3. **Initiate LLM**
   - Creates the chat model via `helpers.get_llm(...)`.
4. **Invoke the Chain**
   - Builds and runs:
     - `sql_chain_with_llm_router(...)`
     - `sql_chain_with_embedding_router(...)`
     - `sql_chain_with_two_store(...)`
   - Each chain routes the question and produces a final answer.

## Notes

- Requires `POSTGRES_CONNECTION_STRING` and Qdrant connectivity.
- The “two store” setup is useful when you want structured answers backed by SQL while also maintaining unstructured document access.

