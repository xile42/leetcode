class Solution:

    def pushDominoes(self, dominoes: str) -> str:

        n = len(dominoes)
        left = ["."] * n
        left_pos = [None] * n
        right = ["."] * n
        right_pos = [None] * n

        cur = "."
        curi = None
        for i in range(n - 1, -1, -1):
            right[i] = cur if dominoes[i] == "." else dominoes[i]
            cur = "." if dominoes[i] == "R" else (cur if dominoes[i] == "." else dominoes[i])
            if dominoes[i] == "L":
                curi = i
            if right[i] == "L":
                right_pos[i] = curi

        cur = "."
        curi = None
        for i in range(n):
            left[i] = cur if dominoes[i] == "." else dominoes[i]
            cur = "." if dominoes[i] == "L" else (cur if dominoes[i] == "." else dominoes[i])
            if dominoes[i] == "R":
                curi = i
            if left[i] == "R":
                left_pos[i] = curi

        ans = ["."] * n
        for i in range(n):
            if left[i] == "R" and right[i] != "L":
                ans[i] = "R"
            elif left[i] != "R" and right[i] == "L":
                ans[i] = "L"
            elif left[i] == "R" and right[i] == "L":
                left_dis = i - left_pos[i]
                right_dis = right_pos[i] - i
                if left_dis < right_dis:
                    ans[i] = "R"
                elif left_dis > right_dis:
                    ans[i] = "L"

        return "".join(ans)
