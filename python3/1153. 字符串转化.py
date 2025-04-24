class Solution:

    def canConvert(self, str1: str, str2: str) -> bool:

        if len(set(str2)) > 26 or (len(set(str2)) == 26 and str1 != str2):
            return False

        cur = 0
        char_map = dict()
        for i, ite in groupby(str1):
            
            cnt = len(list(ite))
            if len(set(str2[cur:cur+cnt])) > 1:
                return False

            if i in char_map and char_map[i] != str2[cur]:
                return False
            char_map[i] = str2[cur]

            cur += cnt

        return True
