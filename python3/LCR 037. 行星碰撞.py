class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def collide(a, b):

            if abs(a) > abs(b):
                return a
            elif abs(a) < abs(b):
                return b
            else:
                return None

        ans = list()
        st = list()
        for v in asteroids:
            if not st:
                if v < 0:
                    ans.append(v)
                else:
                    st.append(v)
            else:
                if v < 0:
                    while st and v and st[-1] * v < 0:
                        v = collide(st.pop(-1), v)
                    if v is None:
                        continue
                    elif v < 0:
                        ans.append(v)
                    else:
                        st.append(v)
                else:
                    st.append(v)

        if st:
            ans += st

        return ans
