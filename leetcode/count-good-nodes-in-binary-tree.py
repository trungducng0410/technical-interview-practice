# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, maxValue):
            nonlocal count

            if root.val >= maxValue:
                count += 1

            if root.left:
                dfs(root.left, max(maxValue, root.left.val))

            if root.right:
                dfs(root.right, max(maxValue, root.right.val))

        dfs(root, root.val)
        return count


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxValue):
            if not root:
                return 0

            res = 1 if root.val >= maxValue else 0
            maxValue = max(maxValue, root.val)
            res += dfs(root.left, maxValue)
            res += dfs(root.right, maxValue)

            return res

        return dfs(root, root.val)
