class Solution:

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        results = [0] * num_people

        idx = 0
        while candies > 0:
            this_candie = min(candies, idx+1)
            candies -= this_candie
            results[idx % num_people] += this_candie
            idx += 1

        return results
