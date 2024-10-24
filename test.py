from helpers import get_total_cost
from datetime import datetime as dt


print(
    get_total_cost(
        chatbot_name="claude-3-5-sonnet-20240620",
        from_date=dt.strptime("2024/07/10", "%Y/%m/%d"),
        to_date=dt.strptime("2024/08/01", "%Y/%m/%d"),
    )
)
