class Solution:

    def canChange(self, start: str, target: str) -> bool:

        if Counter(start) != Counter(target):
            return False

        # 只关心字符依次是什么以及其下标
        ns1 = [[c, i] for i, c in enumerate(start) if c != "_"]
        ns2 = [[c, i] for i, c in enumerate(target) if c != "_"]

        for (c1, i1), (c2, i2) in zip(ns1, ns2):
            if c1 != c2:  # 字符不等一定不行
                return False
            if (c1 == "L" and i2 > i1) or (c1 == "R" and i2 < i1):  # 字符相等下标不符合大小关系也不行
                return False

        return True
