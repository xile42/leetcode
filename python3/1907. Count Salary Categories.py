import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    count = [0] * 3
    for value in accounts["income"]:
        if value < 20000:
            count[0] += 1
        elif value > 50000:
            count[2] += 1
        else:
            count[1] += 1

    return pd.DataFrame({
        "category": ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count": count
    })

