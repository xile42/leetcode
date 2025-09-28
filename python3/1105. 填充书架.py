class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n = len(books)

        @cache
        def f(i):

            if i == n:
                return 0

            ans = inf
            cur_thick = 0
            cur_height = 0
            for j in range(i, n):
                thick, height = books[j]
                if cur_thick + thick > shelfWidth:
                    break
                cur_thick += thick
                cur_height = max(cur_height, height)
                ans = min(ans, cur_height + f(j + 1))

            return ans

        ans = f(0)
        f.cache_clear()

        return ans
