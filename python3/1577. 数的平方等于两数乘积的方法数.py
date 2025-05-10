class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        ans = 0
        nums1.sort()
        nums2.sort()

        for tar in nums1:
            tar *= tar
            left = 0
            right = len(nums2) - 1
            while left < right:
                v = nums2[left] * nums2[right]
                if v == tar:
                    if nums2[left] == nums2[right]:
                        ans += (right - left + 1) * (right - left) // 2
                        break
                    else:
                        cnt_left = cnt_right = 1
                        while nums2[left] == nums2[left + 1]:
                            left += 1
                            cnt_left += 1
                        while nums2[right] == nums2[right - 1]:
                            right -= 1
                            cnt_right += 1
                        ans += cnt_left * cnt_right
                        left += 1
                        right -= 1
                elif v < tar:
                    left += 1
                else:
                    right -= 1

        for tar in nums2:
            tar *= tar
            left = 0
            right = len(nums1) - 1
            while left < right:
                v = nums1[left] * nums1[right]
                if v == tar:
                    if nums1[left] == nums1[right]:
                        ans += (right - left + 1) * (right - left) // 2
                        break
                    else:
                        cnt_left = cnt_right = 1
                        while nums1[left] == nums1[left + 1]:
                            left += 1
                            cnt_left += 1
                        while nums1[right] == nums1[right - 1]:
                            right -= 1
                            cnt_right += 1
                        ans += cnt_left * cnt_right
                        left += 1
                        right -= 1
                elif v < tar:
                    left += 1
                else:
                    right -= 1

        return ans
