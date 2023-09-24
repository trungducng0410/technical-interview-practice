class StackByArray:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackByLinkedList:
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head == None:
            return None

        deletedNode = self.head
        self.head = self.head.next
        deletedNode.next = None

        return deletedNode

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

        return newNode

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.head == None
