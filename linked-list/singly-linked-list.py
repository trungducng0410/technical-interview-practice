class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index == 0:
            return self.getFirst()
        elif index == self.size - 1:
            return self.getLast()
        elif index >= self.size:
            return None

        pointer = self.head
        for i in range(index):
            pointer = pointer.next

        return pointer.value

    def getFirst(self):
        return self.head.value

    def getLast(self):
        if self.head == None:
            return None

        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        return pointer.value

    def add(self, index, value):
        if index == 0:
            return self.addFirst(value)
        elif index >= self.size:
            return self.addLast(value)

        newNode = Node(value)
        pointer = self.head
        for i in range(index - 1):
            pointer = pointer.next

        nextNode = pointer.next
        pointer.next = newNode
        newNode.next = nextNode

        self.size += 1
        return newNode.value

    def addFirst(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

        return newNode.value

    def addLast(self, value):
        if self.head == None:
            return self.addFirst(value)

        newNode = Node(value)
        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
        pointer.next = newNode
        self.size += 1

        return newNode.value

    def remove(self, index):
        if index == 0:
            return self.removeFirst()
        elif index >= self.size - 1:
            return self.removeLast()

        pointer = self.head
        for i in range(index - 1):
            pointer = pointer.next

        removedNode = pointer.next
        pointer.next = removedNode.next
        removedNode.next = None

        self.size -= 1
        return removedNode.value

    def removeFirst(self):
        if self.head == None:
            return None

        oldHead = self.head
        newHead = self.head.next

        oldHead.next = None
        self.head = newHead

        self.size -= 1
        return oldHead.value

    def removeLast(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            return self.removeFirst()

        pointer = self.head
        while pointer.next != None and pointer.next.next != None:
            pointer = pointer.next
        pointer.next = None

        self.size -= 1
        return pointer.value

    def getSize(self):
        return self.size

    def toString(self):
        if self.head == None:
            print("size:", self.size)
            return

        chars = []
        pointer = self.head
        while pointer != None:
            chars.append(str(pointer.value))
            chars.append("->")
            pointer = pointer.next

        print("size:", self.size)
        print("".join(chars))


test = SinglyLinkedList()

test.toString()

test.addFirst(3)
test.addFirst(2)
test.addFirst(1)

test.toString()

test.addLast(4)
test.addLast(5)
test.addLast(6)

test.toString()

test.add(0, 0)
test.add(100, 7)

test.toString()

test.add(1, 100)
test.add(8, 100)
test.add(4, 100)

test.toString()

test.removeFirst()
test.removeFirst()

test.toString()

test.removeLast()
test.removeLast()

test.toString()

test.remove(0)
test.remove(5)

test.toString()

test.remove(1)

test.toString()

print(test.getSize())
print(test.getFirst())
print(test.getLast())
print(test.get(0))
print(test.get(1))
print(test.get(2))
print(test.get(3))
print(test.get(4))
