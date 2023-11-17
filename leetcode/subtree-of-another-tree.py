# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Brute force
# Time complexity: O(n * m) - n is number of node in tree, m is number of node in subtree
# Space complexity: O(h) - height of bigger tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Brute force
# Time complexity: O(n + m) - n is number of node in tree, m is number of node in subtree
# Space complexity: O(h) - height of bigger tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootStr = self.toString(root)
        subStr = self.toString(subRoot)

        return subStr in rootStr

    def toString(self, root) -> bool:
        if root:
            return "#" + str(root.val) + str(self.toString(root.left)) + str(self.toString(root.right))
