class Solution:

    def fizzBuzz(self, n: int) -> List[str]:

        results = list()
        for idx in range(1, n+1):
            if idx % 3 == 0 and idx % 5 == 0:
                result = "FizzBuzz"
            elif idx % 3 == 0:
                result = "Fizz"
            elif idx % 5 == 0:
                result = "Buzz"
            else:
                result = str(idx)
            results.append(result)

        return results
