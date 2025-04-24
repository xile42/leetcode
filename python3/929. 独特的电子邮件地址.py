class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:

        r = list()
        for e in emails:
            a, b = e.split("@")
            if "+" in a:
                a = a.split("+")[0]
            a = a.replace(".", "")
            r.append(a + "@" + b)

        return len(set(r))
