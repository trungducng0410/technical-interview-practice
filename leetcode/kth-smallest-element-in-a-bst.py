# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        # in-order traverse
        def dfs(root):
            if not root:
                return

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)

        return res[k - 1]
