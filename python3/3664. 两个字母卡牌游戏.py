class Solution:

    def score(self, cards: List[str], x: str) -> int:

        c1 = list()
        c2 = list()
        c3 = 0
        tar = x + x
        for s in cards:
            if s == tar:
                c3 += 1
                continue
            if s[0] == x:
                c1.append(s)
            elif s[1] == x:
                c2.append(s)

        l1 = len(c1)
        l2 = len(c2)

        if l1 > 0:
            cnt1 = Counter(c1)
            mx1 = max(cnt1.values())
            if 2 * mx1 > l1:
                ans1 = l1 - mx1
            else:
                ans1 = l1 // 2
        else:
            ans1 = 0

        if l2 > 0:
            cnt2 = Counter(c2)
            mx2 = max(cnt2.values())
            if 2 * mx2 > l2:
                ans2 = l2 - mx2
            else:
                ans2 = l2 // 2
        else:
            ans2 = 0

        ans = l1 + l2
        mx = min(ans1 + ans2, ans // 2)

        mx_ans = 0
        for s in range(0, mx + 1):
            this_ans = s + min(c3, ans - 2 * s)
            if this_ans > mx_ans:
                mx_ans = this_ans

        return mx_ans

        # c1.sort()
        # c2.sort()
        #
        # ans1 = ans2 = 0
        #
        # i = 0
        # j = len(c1) - 1
        # while i < j and c1[i] != c1[j]:
        #     ans1 += 1
        #     i += 1
        #     j -= 1
        #
        # i = 0
        # j = len(c2) - 1
        # while i < j and c2[i] != c2[j]:
        #     ans2 += 1
        #     i += 1
        #     j -= 1
        #
        # left = len(c1) - 2 * ans1 + len(c2) - 2 * ans2
        # ans3 = min(left, c3)
        #
        # ans = ans1 + ans2 + ans3
        #
        # return ans
