class Solution:

    def goodsOrder(self, goods: str) -> List[str]:

        return list(set(["".join(cs) for cs in permutations(list(goods), len(goods))]))
