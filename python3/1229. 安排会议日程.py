class Solution:

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        valid1, valid2 = list(), list()

        for s, e in slots1:
            if e - s >= duration:
                valid1.append((s, e))

        for s, e in slots2:
            if e - s >= duration:
                valid2.append((s, e))

        valid1.sort()
        valid2.sort()

        i = j = 0
        while i < len(valid1) and j < len(valid2):
            s1, e1 = valid1[i]
            s2, e2 = valid2[j]

            if e1 <= s2:
                i += 1
            elif e2 <= s1:
                j += 1
            else:
                start = max(s1, s2)
                end = min(e1, e2)

                if end - start >= duration:
                    return [start, start + duration]

                if e1 < e2:
                    i += 1
                else:
                    j += 1

        return list()