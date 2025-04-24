import pandas as pd


def find_topic(keywords: pd.DataFrame, posts: pd.DataFrame) -> pd.DataFrame:

    tw = keywords.values
    tw = [[t, w.lower()] for t, w in tw]
    pc = posts.values

    results = list()
    for post_id, content in pc:
        result = set()
        content = content.lower()
        for topic_id, word in tw:
            if word in content.split(" "):
                result.add(topic_id)
        result = "Ambiguous!" if len(result) == 0 else ",".join(list(map(str, sorted(result))))
        results.append([post_id, result])

    df = pd.DataFrame({"post_id": [i[0] for i in results], "topic": [i[1] for i in results]})

    return df
