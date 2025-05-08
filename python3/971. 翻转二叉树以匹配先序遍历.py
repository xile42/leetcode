# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        ans = list()
        success = True

        def f(node, i):

            nonlocal success, ans
            if node is None or not success:
                return 0

            if node.val != voyage[i]:
                success = False
                return 1

            flip = False
            cnt = 1
            if node.left and node.left.val != voyage[i + 1]:
                flip = True
                if node.right and node.right.val != voyage[i + 1]:
                    success = False
                    return 1
                else:
                    flip = True
                    ans.append(node.val)
                    cnt += f(node.right, i + cnt)
            else:
                cnt += f(node.left, i + cnt)
            if flip:
                cnt += f(node.left, i + cnt)
            else:
                cnt += f(node.right, i + cnt)

            return cnt

        f(root, 0)

        return [-1] if not success else ans
