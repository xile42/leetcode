import pandas as pd


def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:

    valid_tiv = insurance.groupby(by="tiv_2015", as_index=False)["pid"].count()
    valid_tiv = valid_tiv[valid_tiv["pid"] >= 2]["tiv_2015"]
    insurance["ll"] = insurance.apply(axis=1, func=lambda x: str(x["lat"])+str(x["lon"]))
    valid_ll = insurance.groupby(by="ll", as_index=False)["pid"].count()
    valid_ll = valid_ll[valid_ll["pid"] == 1]["ll"]

    value = insurance[(insurance["ll"].isin(valid_ll)) & (insurance["tiv_2015"].isin(valid_tiv))]["tiv_2016"].sum().round(2)

    return pd.DataFrame({
        "tiv_2016": [value]
    })
