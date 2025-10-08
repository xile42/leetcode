class Solution:

    def removeSubstring(self, s: str, k: int) -> str:

        st = list()
        pattern = "(" * k + ")" * k
        idx = 0
        history_idx = list()
        for c in s:
            if c == pattern[idx]:
                idx += 1
                if idx == len(pattern):
                    st = st[:-2 * k + 1]
                    history_idx = history_idx[:-2 * k + 1]
                    idx = history_idx[-1] if history_idx else 0
                else:
                    st.append(c)
                    history_idx.append(idx)
            else:
                if c == "(":
                    if idx == k:
                        history_idx.append(idx)
                    else:
                        idx = 1
                        history_idx.append(idx)
                else:
                    idx = 0
                    history_idx.append(idx)
                st.append(c)

        return "".join(st)
