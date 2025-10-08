class Solution:

    def generateSchedule(self, n: int) -> List[List[int]]:

        matches = [(i, j) for i in range(n) for j in range(n) if i != j]
        s = set(matches)
        ans = list()
        success = False

        def f():

            nonlocal success
            if success:
                return

            if not s:
                success = True
                return

            if not ans:
                cur = matches[0]
                ans.append(list(cur))
                s.remove(cur)
                f()
            else:
                last = ans[-1]
                for cur in list(s):
                    if cur[0] != last[0] and cur[0] != last[1] and cur[1] != last[0] and cur[1] != last[1]:
                        ans.append(list(cur))
                        s.remove(cur)
                        f()
                        if success:
                            return
                        ans.pop()
                        s.add(cur)

        f()

        return list() if not success else ans
