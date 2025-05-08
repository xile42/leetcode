class Solution:

    def maskPII(self, s: str) -> str:

        if "@" in s:
            s = s.lower()
            head, tail = s.split("@")
            head = head[0] + "*****" + head[-1]
            return "@".join([head, tail])
        else:
            ss = str()
            for c in s:
                if c.isdigit():
                    ss += c
            s = ss
            tail = s[-10:]
            head = s[:-10]
            l = len(head)
            if l == 0:
                return "-".join(["***", "***", tail[6:]])
            elif l == 1:
                return  "-".join(["+*", "***", "***", tail[6:]])
            elif l == 2:
                return "-".join(["+**", "***", "***", tail[6:]])
            else:
                return "-".join(["+***", "***", "***", tail[6:]])
