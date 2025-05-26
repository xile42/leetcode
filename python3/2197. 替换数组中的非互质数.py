class Solution:

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        st = list()
        for v in nums:
            if not st or gcd(st[-1], v) == 1:
                st.append(v)
                continue
            while st and gcd(st[-1], v) != 1:
                v = lcm(st.pop(-1), v)
            st.append(v)

        return st
