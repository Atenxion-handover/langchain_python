from .custom_types import _VECTOR_DB, _EMBEDDING_TYPES, _HYBRID_SEARCH_TYPES
from typing import Optional, Dict
from langchain_core.retrievers import RetrieverLike
from langchain.retrievers import EnsembleRetriever
from .vector_store import get_vector_store_instance
from .embedding_models import get_embedding_model
from langchain_elasticsearch import ElasticsearchRetriever
from .config import Config


def get_retriever(
    index_name: str,
    embedding_model: _EMBEDDING_TYPES,
    vector_db: _VECTOR_DB = "chromadb",
    dimension: Optional[int] = None,
    top_k: int = 4,
    score_threshold: float = 0.01,
    hybrid_search: bool = False,
    **kwargs
) -> RetrieverLike:
    vector_store = get_vector_store_instance(
        embedding_model=embedding_model,
        index_name=index_name,
        dimension=dimension,
        vector_db=vector_db,
        hybrid_search=hybrid_search,
        **kwargs,
    )

    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": top_k, "score_threshold": score_threshold},
    )

    return retriever
