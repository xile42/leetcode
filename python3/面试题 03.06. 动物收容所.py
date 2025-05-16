class AnimalShelf:

    def __init__(self):
        self.t = 0
        self.cat = list()
        self.dog = list()

    def enqueue(self, animal: List[int]) -> None:
        _id, t = animal
        if t == 0:
            heappush(self.cat, [self.t, _id])
        else:
            heappush(self.dog, [self.t, _id])
        self.t += 1

    def dequeueAny(self) -> List[int]:

        cat = [inf, inf]
        dog = [inf, inf]
        if self.cat:
            cat = heappop(self.cat)
        if self.dog:
            dog = heappop(self.dog)

        if cat[0] == dog[0] and cat[0] == inf:
            return [-1, -1]

        if cat[0] < dog[0]:
            ans = [cat[1], 0]
            if dog[0] != inf:
                heappush(self.dog, dog)
        else:
            ans = [dog[1], 1]
            if cat[0] != inf:
                heappush(self.cat, cat)

        return ans

    def dequeueDog(self) -> List[int]:

        if self.dog:
            dog = heappop(self.dog)
            ans = [dog[1], 1]
        else:
            ans = [-1, -1]

        return ans

    def dequeueCat(self) -> List[int]:

        if self.cat:
            cat = heappop(self.cat)
            ans = [cat[1], 0]
        else:
            ans = [-1, -1]

        return ans

# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()