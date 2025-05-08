class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        c = Counter()
        for raw in cpdomains:
            cnt, ip = raw.split(" ")
            cnt = int(cnt)
            c[ip] += cnt
            while (i := ip.find(".")) != -1:
                ip = ip[i + 1:]
                c[ip] += cnt

        return ["{} {}".format(v, k) for k, v in c.items()]
