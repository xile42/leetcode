import pandas as pd


def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:

    friend_request.drop_duplicates(subset=["sender_id", "send_to_id"], inplace=True)
    request_accepted.drop_duplicates(subset=["requester_id", "accepter_id"], inplace=True)

    return pd.DataFrame({
        "accept_rate": [0 if len(friend_request) == 0 else round(len(request_accepted) / len(friend_request), 2)],
    })
