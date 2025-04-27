class Solution:

    def findCommonResponse(self, responses: List[List[str]]) -> str:

        ws = list()
        for response in responses:
            ws += list(set(response))

        return sorted([[-v, k] for k, v in Counter(ws).items()])[0][1]
