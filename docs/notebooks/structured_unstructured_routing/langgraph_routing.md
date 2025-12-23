# `structured_unstructured_routing/langgraph_routing.ipynb`

Notebook: `structured_unstructured_routing/langgraph_routing.ipynb`

## What it does

Implements the structured-vs-unstructured routing pattern as a LangGraph state machine:

- First node classifies the question as **STRUCTURED** or **UNSTRUCTURED**.
- Then routes to either:
  - an SQL chain (generate query → execute → answer), or
  - a RAG chain (retrieve → answer).

## Workflow (step-by-step)

1. **Import Necessary Modules**
   - Imports LangGraph primitives (`StateGraph`, `MessagesState`) and LangChain SQL utilities.
2. **Configure Database**
   - Creates a Postgres SQLAlchemy engine via `Config.POSTGRES_CONNECTION_STRING`.
3. **Ingest Data**
   - Loads `./sample_data/brillar_bank_fixed_deposit.xlsx`.
   - Writes each sheet to Postgres tables.
   - Adds a routing document to Qdrant (metadata indicates structured search).
4. **Initiate LLM**
   - Instantiates a chat model via helpers.
5. **Graph nodes**
   - **classification:** LLM decides `STRUCTURED` vs `UNSTRUCTURED`.
   - **sql_chain:** constructs and executes SQL, then answers from results.
   - **rag_chain:** retrieves from vector store and answers from context.
6. **Build and run graph**
   - Connects nodes and executes the graph for sample questions.

## Notes

- Requires `POSTGRES_CONNECTION_STRING` and Qdrant connectivity.
- This notebook is helpful if you want routing behavior to be explicit and inspectable as a state machine.

