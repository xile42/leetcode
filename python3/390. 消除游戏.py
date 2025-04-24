class Solution:
    
    def lastRemaining(self, n: int) -> int:

##        def f(s):
##
##            if len(s) == 1:
##                return s[0]
##
##            return f([s[i] for i in range(len(s)) if i & 1][::-1])
##
##        return f(list(range(1, n+1)))

##        nums = list(range(1, n+1))
##        while len(nums) != 1:
##            nums = [nums[i] for i in range(1, len(nums), 2)][::-1]
##
##        return nums[0]

        head = step = 1
        left = True

        while n > 1:
            if left or n & 1 == 1:
                head += step
            step *= 2
            n //= 2
            left = not left

        return head
            
