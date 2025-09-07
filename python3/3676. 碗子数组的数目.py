class Solution:

    def bowlSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        left = [-1] * n
        right = [n] * n

        st = list()
        for i in range(n):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            else:
                left[i] = -1
            st.append(i)

        st = list()
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            else:
                right[i] = n
            st.append(i)

        ans = 0
        for i in range(n):
            if left[i] != -1 and right[i] != n:
                ans += 1

        return ans
