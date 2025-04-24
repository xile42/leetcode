import pandas as pd


def form_bond(elements: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(elements, elements, how="cross")
    df = df[(df["type_x"] == "Metal") & (df["type_y"] == "Nonmetal")]
    df.rename(columns={"symbol_x": "Metal", "symbol_y": "Nonmetal"}, inplace=True)

    return df[["Metal", "Nonmetal"]]
