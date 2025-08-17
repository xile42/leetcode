class Solution:

    def sampleStats(self, count: List[int]) -> List[float]:

        ans = list()
        n = sum(count)

        for i in range(256):
            if count[i] > 0:
                ans.append(i)
                break

        for i in range(255, -1, -1):
            if count[i] > 0:
                ans.append(i)
                break

        mean = 0
        for i in range(256):
            mean += (count[i] * i) / n
        ans.append(mean)

        tar = ceil(n/ 2)
        cur = 0
        for i, v in enumerate(count):
            cur += v
            if cur >= tar:
                if n & 1:
                    ans.append(i)
                else:
                    if cur == tar:
                        for j in range(i + 1, 256):
                            if count[j] > 0:
                                ans.append((i + j) / 2)
                                break
                    else:
                        ans.append(i)
                break

        ans.append(0)
        mx = -inf
        for i, v in enumerate(count):
            if v > mx:
                mx = v
                ans[-1] = i

        return ans
