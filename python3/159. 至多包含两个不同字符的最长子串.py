class Solution:

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        left = ans = 0
        cnt = defaultdict(int)
        st = set()
        for right in range(len(s)):
            st.add(s[right])
            cnt[s[right]] += 1
            while len(st) > 2:
                cnt[s[left]] -= 1
                if cnt[s[left]] == 0:
                    st.remove(s[left])
                left += 1
            ans = max(ans, right - left + 1)

        return ans
