import pandas as pd


def f(*args):

    s = set(args)
    a, b, c = args[0], args[1], args[2]
    if a + b > c and b + c > a and c + a > b:
        if len(s) == 1:
            return "Equilateral"
        if len(s) == 2:
            return "Isosceles"
        return "Scalene"
    else:
        return "Not A Triangle"


def type_of_triangle(triangles: pd.DataFrame) -> pd.DataFrame:

    triangles["triangle_type"] = triangles.apply(axis=1, func=lambda row: f(row["A"], row["B"], row["C"]))

    return triangles[["triangle_type"]]
