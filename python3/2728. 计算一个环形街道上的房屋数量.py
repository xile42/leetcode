# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:

    def houseCount(self, street: Optional['Street'], k: int) -> int:

        for _ in range(k):
            street.closeDoor()
            street.moveRight()

        ans = 0
        while not street.isDoorOpen():
            street.openDoor()
            ans += 1
            street.moveRight()

        return ans
