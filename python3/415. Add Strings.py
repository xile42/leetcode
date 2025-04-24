class Solution:

    def addStrings(self, num1: str, num2: str) -> str:

        results = list()
        if len(num1) >= len(num2):
            num1, num2 = num2, num1

        num1 = num1[::-1]
        num2 = num2[::-1]

        c = 0
        for idx in range(len(num1)):
            a, b = num1[idx], num2[idx]
            result = ord(a) + ord(b) - 2 * ord("0") + c
            if result >= 10:
                results.append(str(result % 10))
                c = 1
            else:
                results.append(str(result))
                c = 0

        for idx in range(len(num1), len(num2)):
            a = num2[idx]
            result = ord(a) - ord("0") + c
            if result >= 10:
                results.append(str(result % 10))
                c = 1
            else:
                results.append(str(result))
                c = 0

        if c == 1:
            results.append("1")

        return "".join(results)[::-1]
