class Solution:

    def decodeMessage(self, key: str, message: str) -> str:

        d = str()
        for c in key:
            if c.isalpha()and c not in d:
                d += c
        d = {k: v for k, v in zip(d, string.ascii_lowercase)}

        return "".join([c if c not in d else d[c] for c in message])
