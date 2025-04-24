import pandas as pd


def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:

    df = calls.copy()
    df["from_id"] = calls["to_id"]
    df["to_id"] = calls["from_id"]

    df = pd.concat([calls, df])
    df["call_count"] = 1
    df = df[df["from_id"] < df["to_id"]].groupby(by=["from_id", "to_id"], as_index=False).agg({
        "call_count": "sum",
        "duration": "sum",
    })
    df.rename(columns={
        "from_id": "person1",
        "to_id": "person2",
        "duration": "total_duration",
    }, inplace=True)

    return df
