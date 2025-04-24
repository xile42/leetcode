class Solution:

    def countSeniors(self, details: List[str]) -> int:

        return sum(i[-4:-2] > "60" for i in details)
