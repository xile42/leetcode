class Solution:

    def distMoney(self, money: int, children: int) -> int:

        if money < children:
            return -1

        ans = 0
        left = money - children
        can = min(left // 7, children)
        left = left - can * 7
        ans += can
        if left == 3 and children - can == 1:
            ans -= 1
        if left > 0 and children - can == 0:
            ans -= 1

        return ans
