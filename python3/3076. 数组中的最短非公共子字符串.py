class Solution:

    def shortestSubstrings(self, arr: List[str]) -> List[str]:

        ans = list()
        for i, s in enumerate(arr):
            cur_ans = ""
            invalid = set()
            for l in range(1, len(s) + 1):
                for start in range(len(s)):
                    sub_s = s[start:start + l]
                    if len(sub_s) != l:
                        break
                    if sub_s in invalid:
                        continue
                    for j, ss in enumerate(arr):
                        if i == j:
                            continue
                        if sub_s in ss:
                            invalid.add(sub_s)
                            break
                    else:
                        cur_ans = sub_s if cur_ans == "" else min(cur_ans, sub_s)
                if cur_ans != "":
                    break
            ans.append(cur_ans)

        return ans
