import pandas as pd


def f(x):

    p, f = x["power"], x["factor"]
    
    if f == 0:
        return str()

    sf = "+{}".format(f) if f > 0 else str(f)

    if p == 0:
        sp = str()
    elif p == 1:
        sp = str()
    else:
        sp = "^{}".format(p)

    if p == 0:
        return sf

    return "{}X{}".format(sf, sp)


def build_the_equation(terms: pd.DataFrame) -> pd.DataFrame:

    df = terms.sort_values("power", ascending=False)
    df["s"] = df.apply(axis=1, func=f)
    ans = "".join(df["s"].tolist()) + "=0"

    return pd.DataFrame({"equation": [ans]})
    
