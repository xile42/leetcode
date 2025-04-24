import pandas as pd
from functools import reduce


def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:

    return pd.DataFrame({
        "common_perms": [reduce(and_, user_permissions["permissions"])],
        "any_perms": [reduce(or_, user_permissions["permissions"])],
    })

    # return pd.DataFrame({
    #     "common_perms": [reduce(lambda x, y: x & y, user_permissions["permissions"])],
    #     "any_perms": [reduce(lambda x, y: x | y, user_permissions["permissions"])],
    # })

    # values = user_permissions["permissions"].tolist()
    # and_result = values[0]
    # for value in values[1:]:
    #     and_result &= value
    # or_result = values[0]
    # for value in values[1:]:
    #     or_result |= value
    #
    # return pd.DataFrame({"common_perms": [and_result], "any_perms": [or_result]})
