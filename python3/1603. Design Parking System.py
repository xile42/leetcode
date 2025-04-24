class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):

        self.left = {
            1: big,
            2: medium,
            3: small,
        }

    def addCar(self, carType: int) -> bool:

        if self.left[carType] > 0:
            self.left[carType] -= 1
            return True
        return False
