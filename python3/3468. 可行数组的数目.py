class Solution:

    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:

        # def f(s, e, ss, ee):
        #
        #     if e < ss or ee < s:
        #         return 0
        #
        #     if ss <= s and e <= ee:
        #         return e - s + 1
        #
        #     if s <= ss and ee <= e:
        #         return ee - ss + 1
        #
        #     if s < ss:
        #         return e - ss + 1
        #
        #     if e > ee:
        #         return ee - s + 1

        diff = [original[i] - original[i - 1] for i in range(1, len(original))]
        pre_s, pre_e = bounds[0]
        ans = pre_e - pre_s + 1
        for i in range(1, len(original)):
            s, e = bounds[i]
            d = diff[i - 1]
            tar_s, tar_e = pre_s + d, pre_e + d
            final_s = max(s, tar_s)
            final_e = min(e, tar_e)
            if final_s > final_e:
                ans = 0
                break
            else:
                ans = min(ans, final_e - final_s + 1)
                pre_s, pre_e = final_s, final_e

        return ans
