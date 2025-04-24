class TreeNode:

    def __init__(self, char):

        self.next = dict()
        self.char = char
        self.word = list()


class Solution:

    def generate(self, head, word):

        current = head
        for idx, char in enumerate(word):
            if char not in current.next:
                node = TreeNode(char)
                current.next[char] = node
            current = current.next[char]
            if idx == len(word) - 1:
                current.word.append(word)

    def check(self, head, word):

        count = 0
        current = head
        for idx, char in enumerate(word):
            if char not in current.next:
                return count
            count += 1
            current = current.next[char]

        return count

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        head = TreeNode(None)
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        for word in arr1:
            self.generate(head, str(word))

        max_result = 0
        for word in arr2:
            max_result = max(max_result, self.check(head, str(word)))

        return max_result
