class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def getHeight(node):
    if node == None:
        return 0

    return 1 + max(getHeight(node.left), getHeight(node.right))


def containsNode(root, value):
    if root == None:
        return False

    if value < root.data:
        return containsNode(root.left, value)
    elif value > root.data:
        return containsNode(root.right, value)
    else:
        return True


def addNode(root, value):
    if root == None:
        root = Node(value)
    else:
        if value > root.data:
            root.right = addNode(root.right, value)
        else:
            root.left = addNode(root.left, value)

    return root


def getMinRight(node):
    while node.left != None:
        node = node.left
    return node.data


def removeNode(root, value):
    if value > root.data:
        root.right = removeNode(root.right, value)
    elif value < root.data:
        root.left = removeNode(root.left, value)
    else:
        if root.left == None and root.right == None:
            return None
        elif root.left == None and root.right != None:
            rightNode = root.right
            root.data = None
            root = None
            return rightNode
        elif root.left != None and root.right == None:
            leftNode = root.left
            root.data = None
            root = None
            return leftNode
        else:
            tmp = getMinRight(root.right)
            root.data = tmp
            root.right = removeNode(root.right, tmp)

    return root


class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        self.nodeCount = 0

    def isEmpty(self):
        return self.nodeCount == 0

    def size(self):
        return self.nodeCount

    def height(self):
        return getHeight(self.root)

    def search(self, value):
        return containsNode(self.root, value)

    def add(self, value):
        if self.search(value):
            return False

        self.root = addNode(self.root, value)
        self.nodeCount += 1
        return True

    def remove(self, value):
        if not self.search(value):
            return False

        self.root = removeNode(self.root, value)
        self.nodeCount -= 1
        return True
