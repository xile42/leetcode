import pandas as pd


def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:

    a = salaries[salaries["department"] == "Engineering"]["salary"].max()
    b = salaries[salaries["department"] == "Marketing"]["salary"].max()

    return pd.DataFrame({
        "salary_difference": [abs(a - b)]
    })
