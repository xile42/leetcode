class Solution:

    def distributeCookies(self, cookies: List[int], k: int) -> int:

        all_cookies = list(permutations(cookies))

        def check(x):

            for ns in all_cookies:
                need = 1
                cur = 0
                for c in ns:
                    if cur + c > x:
                        need += 1
                        cur = 0
                    cur += c

                if need <= k:
                    return True

            return False

        left, right = max(cookies), sum(cookies)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
