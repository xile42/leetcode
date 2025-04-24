class Solution:

    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:

        stock.sort()

        return stock[:cnt]
