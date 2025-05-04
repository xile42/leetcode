# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:

    def rand10(self):

        while True:
            i, j = rand7(), rand7()
            v = ((i - 1) * 7) + j
            if 1 <= v <= 10:
                return v
