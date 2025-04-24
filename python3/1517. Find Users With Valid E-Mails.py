import pandas as pd
import string

letters = set(string.ascii_lowercase + string.ascii_uppercase)
valid_chars = set(string.ascii_lowercase + string.ascii_uppercase + string.digits + "_.-")
host_string = "leetcode.com"


def check(mail):

    if len(mail) == 0 or "@" not in mail:
        return 0

    if mail[0] not in letters:
        return 0

    split_result = mail.split("@")
    if len(split_result) != 2:
        return 0
    pre, host = split_result

    if len(set(pre) - valid_chars) != 0:
        return 0

    if host != host_string:
        return 0

    return 1


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:

    users["flag"] = users["mail"].apply(check)
    df = users[users["flag"] == 1][["user_id", "name", "mail"]]

    return df
