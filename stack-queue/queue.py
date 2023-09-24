
from collections import deque


class QueueByDeque:
    def __init__(self):
        self.data = deque([])

    def add(self, value):
        self.data.append(value)

    def remove(self):
        return self.data.popleft()

    def peek(self):
        return self.data[0]

    def isEmpty(self):
        return len(self.data) == 0


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueByLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def remove(self):
        if self.head == None:
            return None
        deletedNode = self.head
        self.head = self.head.next
        deletedNode.next = None

        if self.head == None:
            self.tail = None

        return deletedNode

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.head == None and self.tail == None
