from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_core.retrievers import RetrieverLike
from langchain_cohere import CohereRerank
from typing import Optional, Literal
from .model_mapping import _RERANKERS, _VENDORS
import os

Rerankers = Literal[
    "BAAI/bge-reranker-base",
    "rerank-multilingual-v3.0",
]

Vendors = Literal["huggingface", "cohere"]

reranker_vendors = {
    "BAAI/bge-reranker-base": "huggingface",
    "rerank-multilingual-v3.0": "cohere",
}


def get_reranker(
    base_retriever: RetrieverLike,
    model_name: Rerankers,
    top_k: int = 3,
) -> Optional[ContextualCompressionRetriever]:
    vendor: Vendors = reranker_vendors.get(model_name, "BAAI/bge-reranker-base")
    match vendor:
        case "huggingface":
            model = HuggingFaceCrossEncoder(model_name=model_name)
            compressor = CrossEncoderReranker(model=model, top_n=top_k)
        case "cohere":
            compressor = CohereRerank(
                model=model_name,
                cohere_api_key=os.getenv("COHERE_API_KEY"),
                top_n=top_k,
            )
        case _:
            print("Reanker Error")
            return

    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, base_retriever=base_retriever
    )

    return compression_retriever
