class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        cs = list()
        ds = list()
        for s in logs:
            if s[-1].isalpha():
                cs.append([s.split(" ")[0], " ".join(s.split(" ")[1:]), s])
            else:
                ds.append(s)

        cs.sort(key=lambda x: [x[1], x[0]])

        return [i[-1] for i in cs] + ds
