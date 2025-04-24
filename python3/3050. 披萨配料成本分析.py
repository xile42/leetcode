import pandas as pd


def cost_analysis(toppings: pd.DataFrame) -> pd.DataFrame:

    toppings = toppings.sort_values("topping_name").reset_index()
    toppings["id"] = toppings.index
    df = pd.merge(pd.merge(toppings, toppings, "cross"), toppings, "cross")
    df = df[(df["id_x"] < df["id_y"]) & (df["id_y"] < df["id"])]
    df["pizza"] = df.apply(axis=1, func=lambda x: ",".join([x["topping_name_x"], x["topping_name_y"], x["topping_name"]]))
    df["total_cost"] = df.apply(axis=1, func=lambda x: x["cost_x"] + x["cost_y"] + x["cost"]).round(2)
    df = df.sort_values(["total_cost", "pizza"], ascending=[False, True])

    return df[["pizza", "total_cost"]]
    
