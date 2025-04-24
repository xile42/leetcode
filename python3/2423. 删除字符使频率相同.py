class Solution:

    def equalFrequency(self, word: str) -> bool:

        for i in range(len(word)):  # 枚举删除的字符
            cnt = Counter(word[:i] + word[i + 1:])  # 统计出现次数
            if len(set(cnt.values())) == 1:  # 出现次数都一样
                return True

        return False
