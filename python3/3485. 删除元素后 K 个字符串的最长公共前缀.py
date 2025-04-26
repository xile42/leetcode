class Node:

    __slots__ = "son", "end", "depth", "ids"

    def __init__(self, depth, _id):

        self.son = {}
        self.ids = {_id}  # 哪些下标的字符串对这个Node有贡献
        self.depth = depth
        self.end = False


class Trie:

    def __init__(self):

        self.root = Node(depth=0, _id=None)
        self.candidates = list()

    def insert(self, word: str, word_idx) -> None:

        cur = self.root
        depth = 1
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node(depth=depth, _id=word_idx)
            else:
                cur.son[c].ids.add(word_idx)
            cur = cur.son[c]
            depth += 1
        cur.end = True

    def find(self, word: str) -> int:

        cur = self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur = cur.son[c]

        return 2 if cur.end else 1

    def search(self, word: str) -> bool:

        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:

        return self.find(prefix) != 0

    def solve(self, cur, k, idx):  # 超时！！  ~~>.<~~

        # print("[solve] cur.son: {}, cur.ids: {}, cur.depth: {}, idx: {}".format(list(cur.son.keys()), cur.ids, cur.depth, idx))
        ans = 0
        for child in cur.son.values():
            v = len(child.ids) if idx not in child.ids else len(child.ids) - 1
            if v >= k:
                # print("[recursion] v: {}, child.ids: {}".format(v, child.ids))
                ans = max(ans, child.depth)
                ans = max(ans, self.solve(child, k, idx))

        return ans

    def prepare(self, cur, k):  # 找所有 >= k的点

        for child in cur.son.values():
            v = len(child.ids)
            if v >= k:
                self.candidates.append([child.depth, child.ids])
                self.prepare(child, k)

    def solve2(self, idx, k):

        for d, ids in self.candidates:
            if len(ids) >= k + 1 or len(ids) == k and idx not in ids:
                return d

        return 0


class Solution:

    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:

        if len(words) <= k:
            return [0] * len(words)

        trie = Trie()
        for idx, word in enumerate(words):
            trie.insert(word, idx)

        # 超时
        # ans = [0] * len(words)
        # for idx in range(len(words)):
        #     ans[idx] = trie.solve(trie.root, k, idx)
        #
        # return ans

        # 预处理
        trie.prepare(trie.root, k)
        trie.candidates = sorted(trie.candidates, reverse=True, key=lambda x: x[0])
        ans = [0] * len(words)
        for idx in range(len(words)):
            ans[idx] = trie.solve2(idx, k)

        return ans
