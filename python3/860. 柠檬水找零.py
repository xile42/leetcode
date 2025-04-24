class Solution:

    def lemonadeChange(self, bills: List[int]) -> bool:

        cur = defaultdict(int)

        def f(tar):

            nonlocal cur
            
            if tar == 0:
                return True

            for v in [10, 5]:
                while tar >= v and cur[v]:
                    tar -= v
                    cur[v] -= 1

            if tar == 0:
                return True

            return False

        for bill in bills:
            if f(bill - 5):
                cur[bill] += 1
            else:
                return False

        return True
