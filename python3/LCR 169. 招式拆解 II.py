class Solution:

    def dismantlingAction(self, arr: str) -> str:

        for k, v in Counter(arr).items():
            if v == 1:
                return k

        return " "
