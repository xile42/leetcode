class Solution:

    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:

        c = Counter()
        for m, s in zip(messages, senders):
            c[s] += len(m.split(" "))

        mx = max(c.values())
        ans = [k for k in c if c[k] == mx]

        return sorted(ans)[-1]
