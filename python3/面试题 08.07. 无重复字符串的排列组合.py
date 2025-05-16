class Solution:

    def permutation(self, S: str) -> List[str]:

        if not S:
            return list()

        return ["".join(cs) for cs in permutations(list(S))]
