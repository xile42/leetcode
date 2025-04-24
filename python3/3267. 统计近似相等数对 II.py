class Solution:

    def countPairs(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        cnt = Counter()
        ans = 0
        for idx in range(n):
            sn = str(nums[idx])
            sln = list(sn)
            candidates = {nums[idx]}
            for i in range(len(sln)):
                for j in range(i + 1, len(sln)):
                    sln[i], sln[j] = sln[j], sln[i]
                    candidates.add(int("".join(sln)))
                    for p in range(i + 1, len(sln)):
                        for q in range(p + 1, len(sln)):
                            sln[p], sln[q] = sln[q], sln[p]
                            candidates.add(int("".join(sln)))
                            sln[p], sln[q] = sln[q], sln[p]
                    sln[i], sln[j] = sln[j], sln[i]
            ans += sum(cnt[i] for i in candidates)
            cnt[nums[idx]] += 1

        return ans
