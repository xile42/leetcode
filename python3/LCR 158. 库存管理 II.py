class Solution:

    def inventoryManagement(self, stock: List[int]) -> int:

        c = Counter(stock)
        for k, v in c.items():
            if v > len(stock) / 2:
                return k
