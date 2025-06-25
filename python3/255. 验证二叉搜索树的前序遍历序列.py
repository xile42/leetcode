class Solution:

    def verifyPreorder(self, preorder: List[int]) -> bool:

        stack = list()
        min_val = -inf
        for num in preorder:
            if num <= min_val:
                return False
            while stack and num > stack[-1]:
                min_val = stack.pop()
            stack.append(num)

        return True
