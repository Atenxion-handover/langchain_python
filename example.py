from helpers import (
    create_conversational_retrieval_chain,
    invoke_conversational_retrieval_chain,
    get_retriever,
    get_llm,
    get_reranker,
)

retriever = get_retriever(
    index_name="test",
    embedding_model="text-embedding-3-large",
    dimension=256,
    vector_db="qdrant",
    hybrid_search=False,
)

llm = get_llm(model_name="gpt-4o-mini", temperature=0.5)
chain = create_conversational_retrieval_chain(
    llm=llm, retriever=retriever, instruction=None
)

result = invoke_conversational_retrieval_chain(chain, "what is fixed deposit")
