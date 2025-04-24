import pandas as pd


def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:

    df = activity.groupby(by=["machine_id", "process_id"], as_index=False)["timestamp"].agg(lambda x: abs(x.tolist()[0]-x.tolist()[1]))
    df = df.groupby(by="machine_id", as_index=False)["timestamp"].mean()
    df["timestamp"] = df["timestamp"].round(3)
    df.rename(columns={"timestamp": "processing_time"}, inplace=True)

    return df
