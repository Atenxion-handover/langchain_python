from langfuse import Langfuse
from .config import Config
from typing import Optional
import datetime as dt


def get_total_cost(
    chatbot_name: str,
    from_timestamp: Optional[dt.datetime] = None,
    to_timestamp: Optional[dt.datetime] = None,
) -> float:
    langfuse = Langfuse(
        public_key=Config.LANGFUSE_PUBLIC_KEY,
        secret_key=Config.LANGFUSE_SECRET_KEY,
        host=Config.LANGFUSE_BASEURL,
    )

    langfuse_config = {
        "user_id": chatbot_name,
        "from_timestamp": from_timestamp,
        "to_timestamp": to_timestamp,
    }

    total_pages = langfuse.fetch_traces(**langfuse_config).meta.total_pages

    cost = 0
    for page_number in range(0, total_pages):
        traces = langfuse.fetch_traces(page=page_number + 1, **langfuse_config)
        for trace in traces.data:
            cost += trace.total_cost

    rounded_cost = round(cost, 6)
    return rounded_cost
