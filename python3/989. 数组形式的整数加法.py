class Solution:

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        c = k
        n = len(num)
        cur = n - 1
        while cur >= 0 and c:
            s = num[cur] + c
            num[cur] = s % 10
            c = s // 10
            cur -= 1

        if c == 0:
            return num
        else:
            return list(map(int, str(c))) + num
