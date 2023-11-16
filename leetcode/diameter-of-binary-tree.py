# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(n^2)
# Space complexity: O(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxLeft = self.getMaxDepth(root.left, 0)
        maxRight = self.getMaxDepth(root.right, 0)

        return max(maxLeft + maxRight, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def getMaxDepth(self, node, depth):
        if not node:
            return depth

        return max(self.getMaxDepth(node.left, depth + 1), self.getMaxDepth(node.right, depth + 1))



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)

            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res