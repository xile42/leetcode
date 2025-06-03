class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        ans = 0

        have = initialBoxes

        while have:
            next_have = list()
            for i in have:
                if status[i] != 1:
                    next_have.append(i)
                else:
                    for k in keys[i]:
                        status[k] = 1
                    next_have += containedBoxes[i]
                    ans += candies[i]
            if have == next_have:
                break
            have = next_have

        return ans
