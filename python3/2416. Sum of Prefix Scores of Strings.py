class TreeNode:

    def __init__(self):
        self.val = 0
        self.next = dict()


class Solution:

    def generate(self, node, word):

        current = node
        for char in word:
            if char not in current.next:
                current.next[char] = TreeNode()
            current.next[char].val += 1
            current = current.next[char]

    def check(self, node, word):

        current = node
        result = 0
        for char in word:
            current = current.next[char]
            result += current.val

        return result

    def sumPrefixScores(self, words: List[str]) -> List[int]:

        head = TreeNode()
        for word in words:
            self.generate(head, word)

        results = list()
        for word in words:
            results.append(self.check(head, word))

        return results
