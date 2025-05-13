class Solution:

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        t1 = 10 ** 4
        t2 = 10 ** 9
        t3 = 10 ** 2
        f1 = True if max(length, width, height) >= t1 or length * width * height >= t2 else False
        f2 = True if mass >= 100 else False

        if f1 and f2:
            return "Both"
        elif not f1 and not f2:
            return "Neither"
        elif f1:
            return "Bulky"
        else:
            return "Heavy"