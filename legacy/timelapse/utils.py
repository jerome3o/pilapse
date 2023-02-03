from datetime import datetime


def get_time_str() -> str:
    return f"{datetime.now():%Y-%m-%d_%H-%M-%S}"
