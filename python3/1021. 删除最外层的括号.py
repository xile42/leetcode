class Solution:

    def removeOuterParentheses(self, s: str) -> str:

        stack = list()
        ps = list()
        cnt = 0
        for char in s:
            stack.append(char)
            if char == ")":
                cnt -= 1
                if cnt == 0:
                    ps.append("".join(stack[1:-1]))
                    stack = list()
                    cnt = 0
            else:
                cnt += 1

        return "".join(ps)
                
        
