# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Brute force
# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left, right = self.getDepth(root.left), self.getDepth(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, root):
        if not root:
            return 0

        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        return 1 + max(left, right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root):
            if not root:
                return 0
            nonlocal res

            left, right = dfs(root.left), dfs(root.right)

            if abs(left - right) > 1:
                res = False

            return 1 + max(left, right)

        dfs(root)
        return res
