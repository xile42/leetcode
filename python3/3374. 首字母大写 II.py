import pandas as pd


def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:

    df = user_content
    df = df.rename(columns={"content_text": "original_text"})
    df["converted_text"] = df["original_text"].apply(func=lambda x: " ".join([w.title() if "-" not in w else "-".join([sub_w.title() for sub_w in w.split("-")]) for w in x.split(" ")]))

    return df
