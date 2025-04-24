class Node:

    def __init__(self, c):

        self.c = c
        self.children = dict()
        self.end = False


class Trie:

    def __init__(self):

        self.root = Node(None)

    def insert(self, word: str) -> None:

        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur.children[c] = Node(c)
                cur = cur.children[c]
    
        cur.end = True

    def search(self, word: str) -> bool:

        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]

        return cur.end
    
    def startsWith(self, prefix: str) -> bool:

        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            else:
                cur = cur.children[c]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
