class Solution:

    def cellsInRange(self, s: str) -> List[str]:

        cs, ce = s[0], s[3]
        rs, re = s[1], s[4]

        results = list()
        for col in range(ord(cs)-ord("a"), ord(ce)-ord("a")+1):
            for row in range(int(rs), int(re)+1):
                results.append(chr(col + ord("a"))+str(row))

        return results
