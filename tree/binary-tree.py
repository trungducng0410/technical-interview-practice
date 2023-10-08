from collections import deque


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self, root):
        self.root = root

    def printTree(self, type):
        if type == "preorder":
            print(self.preorder_print(self.root, ""))
        elif type == "inorder":
            print(self.inorder_print(self.root, ""))
        elif type == "postorder":
            print(self.postorder_print(self.root, ""))
        elif type == "levelorder":
            print(self.levelorder_print(self.root))
        else:
            print("Traversal type " + str(type) + " is not supported")

    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = deque()
        queue.append(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue[0].value) + "-"
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return traversal


#       1
#      / \
#     2   3
#    / \  / \
#   4   5 6  7
#             \
#              8
root = Node(1)
tree = BinaryTree(root)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.root.right.right.left = Node(8)

tree.printTree("preorder")
tree.printTree("inorder")
tree.printTree("postorder")
tree.printTree("levelorder")
