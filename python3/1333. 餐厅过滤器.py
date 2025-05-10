class Solution:

    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        ans = list()
        for row in restaurants:
            if (veganFriendly == 1 and row[2] != 1) or row[3] > maxPrice or row[4] > maxDistance:
                continue
            ans.append(row)

        ans.sort(key=lambda x: [x[1], x[0]], reverse=True)

        return [row[0] for row in ans]
