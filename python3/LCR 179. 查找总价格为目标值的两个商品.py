class Solution:

    def twoSum(self, price: List[int], target: int) -> List[int]:

        s = set()
        for n in price:
            if target - n in s:
                return [n, target - n]
            s.add(n)

