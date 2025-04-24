class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:

        if not root:
            return
        ans = TreeNode(root.val)
        if root.children:
            ans.left = self.encode(root.children[0])
            cur = ans.left
            for child in root.children[1:]:
                cur.right = self.encode(child)
                cur = cur.right

        return ans

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':

        if not data:
            return
        root = Node(data.val, [])
        if data.left:
            root.children.append(self.decode(data.left))
            cur = data.left
            while cur.right:
                root.children.append(self.decode(cur.right))
                cur = cur.right

        return root
