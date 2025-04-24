class Solution:

    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        ns = sorted(asteroids)
        cur = mass
        for n in ns:
            if cur < n:
                return False
            cur += n

        return True
