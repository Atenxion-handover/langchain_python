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

llm = get_llm(model_name="open-mixtral-8x22b")
chain = create_conversational_retrieval_chain(
    llm=llm, retriever=retriever, instruction=None
)

result = invoke_conversational_retrieval_chain(chain, "what is fixed deposit")
