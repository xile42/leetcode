class Solution:

    def check(self, s):

        stack = list()
        for char in s:
            if char in "([{":
                stack.append(char)
            elif char == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop(-1)
            elif char == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop(-1)
            elif char == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop(-1)

        return True if len(stack) == 0 else False

    def isValid(self, s: str) -> bool:

        return self.check(s)
