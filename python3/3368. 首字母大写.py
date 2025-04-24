import pandas as pd


def process_text(user_content: pd.DataFrame) -> pd.DataFrame:

    df = user_content
    df = df.rename(columns={"content_text": "original_text"})
    df["converted_text"] = df["original_text"].apply(func=lambda x: " ".join([w.title() for w in x.split(" ")]))

    return df
