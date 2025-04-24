import pandas as pd


def func(x):

    l = x["left_value"]
    r = x["right_value"]
    op = x["operator"]
    if op == ">":
        return "true" if l > r else "false"
    elif op == "<":
        return "true" if l < r else "false"
    else:
        return "true" if l == r else "false"


def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:

    variables.rename(columns={"value": "left_value"}, inplace=True)
    df = pd.merge(expressions, variables, how="left", left_on="left_operand", right_on="name")
    variables.rename(columns={"left_value": "right_value"}, inplace=True)
    df = pd.merge(df, variables, how="left", left_on="right_operand", right_on="name")
    df["value"] = df.apply(axis=1, func=func)

    return df[["left_operand", "operator", "right_operand", "value"]]

