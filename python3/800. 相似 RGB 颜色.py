class Solution:

    def similarRGB(self, color: str) -> str:

        a, b, c = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16), 
        max_v = -inf
        max_ijk = None
        for i in range(16):
            iv = i * 16 + i
            for j in range(16):
                jv = j * 16 + j
                for k in range(16):
                    kv = k * 16 + k
                    sim = -(iv - a) ** 2 - (jv - b) ** 2 - (kv - c) ** 2
                    if sim > max_v:
                        max_v = sim
                        max_ijk = (i, j, k)

        cs = list(map(str, list(range(10)))) + ["a", "b", "c", "d", "e", "f"]
        d = {i: c for i, c in enumerate(cs)}
        i, j, k = max_ijk
        return "#{}{}{}{}{}{}".format(d[i], d[i], d[j], d[j], d[k], d[k])
