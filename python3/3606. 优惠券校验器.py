class Solution:

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        valid_s = set(string.ascii_letters + string.digits + "_")
        valid_business = {"electronics", "grocery", "pharmacy", "restaurant"}
        order = ["electronics", "grocery", "pharmacy", "restaurant"]

        ans = list()
        for c, b, a in zip(code, businessLine, isActive):
            if not c or set(c) - valid_s:
                continue
            if b not in valid_business:
                continue
            if not a:
                continue
            ans.append([c, b])

        ans.sort(key=lambda x: (order.index(x[1]), x[0]))

        return [x[0] for x in ans]
