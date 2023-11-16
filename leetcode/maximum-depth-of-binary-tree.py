# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS recursive
# Time complexity: O(n)
# Space complexity: O(d) - max depth
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getMaxDepth(root, 0)

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

# BFS
# Time complexity: O(n)
# Space complexity: O(d) - number of leaf node
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxD = 0
        queue = deque([root])

        while queue:
            maxD += 1
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                if node.right:
                    queue.appendleft(node.right)

        return maxD


# DFS iterative
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxD = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                maxD = max(maxD, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])

        return maxD
