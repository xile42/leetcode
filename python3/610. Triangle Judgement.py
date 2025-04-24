import pandas as pd


def check(args):

    x, y, z = args

    if x+y > z and y+z > x and z+x > y and abs(x-y) < z and abs(y-z) < x and abs(z-x) < y:
        return "Yes"
    return "No"


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:

    triangle["triangle"] = triangle[["x", "y", "z"]].apply(check, axis=1)
    return triangle
