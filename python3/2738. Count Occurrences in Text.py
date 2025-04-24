import pandas as pd


def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:

    files["bull"] = files["content"].apply(lambda x: 1 if " bull " in x else 0)
    files["bear"] = files["content"].apply(lambda x: 1 if " bear " in x else 0)

    return pd.DataFrame({
        "word": ["bull", "bear"],
        "count": [files["bull"].sum(), files["bear"].sum()],
    })
