import pandas as pd


def server_utilization_time(servers: pd.DataFrame) -> pd.DataFrame:

    df = servers.sort_values(["server_id", "status_time"])
    df["time"] = df["status_time"] - df.shift(1)["status_time"]
    df = df[(df["server_id"] == df.shift(1)["server_id"]) & (df["session_status"] == "stop")]
    result = df["time"].sum().total_seconds()  # 或 .days
    result = int(result / (60 * 60 * 24))

    return pd.DataFrame({"total_uptime_days": [result]})    
