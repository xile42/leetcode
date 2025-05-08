class Solution:

    def threeSumMulti(self, arr: List[int], target: int) -> int:

        arr.sort()
        base = 10 ** 9 + 7
        ans = 0
        n = len(arr)
        for k in range(n - 1, 1, -1):
            tar = target - arr[k]
            l, r = 0, k - 1
            while l < r:
                if arr[l] + arr[r] == tar:
                    if arr[l] == arr[r]:
                        ans += comb(r - l + 1, 2) % base
                        l = r
                    else:
                        cl = cr = 1
                        while arr[l] == arr[l + 1]:
                            cl += 1
                            l += 1
                        while arr[r] == arr[r - 1]:
                            cr += 1
                            r -= 1
                        ans += cl * cr % base
                        l += 1
                elif arr[l] + arr[r] > tar:
                    r -= 1
                else:
                    l += 1
            ans %= base

        return ans
