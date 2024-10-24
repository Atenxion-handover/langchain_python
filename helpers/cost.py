from langfuse import Langfuse
from .config import Config


def get_total_cost(chatbot_name):
    langfuse = Langfuse(
        public_key=Config.LANGFUSE_PUBLIC_KEY,
        secret_key=Config.LANGFUSE_SECRET_KEY,
        host=Config.LANGFUSE_BASEURL,
    )

    total_pages = langfuse.fetch_traces(user_id=chatbot_name).meta.total_pages

    cost = 0
    for page_number in range(0, total_pages):
        traces = langfuse.fetch_traces(user_id=chatbot_name, page=page_number + 1)
        for trace in traces.data:
            cost += trace.total_cost

    rounded_cost = round(cost, 6)
    return rounded_cost
