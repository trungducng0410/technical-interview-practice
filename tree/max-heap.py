class MaxHeap:
    def __init__(self):
        self.size = 0
        self.items = []

    def getLeftChildIndex(self, parentIndex):
        return 2 * parentIndex + 1

    def getRightChildIndex(self, parentIndex):
        return 2 * parentIndex + 2

    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def getLeftChild(self, index):
        return self.items[self.getLeftChildIndex(index)]

    def getRightChild(self, index):
        return self.items[self.getRightChildIndex(index)]

    def getParent(self, index):
        return self.items[self.getParentIndex(index)]

    def swap(self, index1, index2):
        self.items[index1], self.items[index2] = self.items[index2], self.items[index1]

    def peek(self):
        if self.size == 0:
            return None

        return self.items[0]

    def poll(self):
        if self.size == 0:
            return None

        item = self.items[-1]
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.size -= 1
        self.heapifyDown()
        return

    def add(self, item):
        self.items.append(item)
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.getParent(index) < self.items[index]:
            self.swap(index, self.getParentIndex(index))
            index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            largerIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.getRightChild(index) > self.getLeftChild(index):
                largerIndex = self.getRightChildIndex(index)

            if self.items[index] < self.items[largerIndex]:
                self.swap(index, largerIndex)

            index = largerIndex

    def display(self):
        print(self.items)


test = MaxHeap()
test.add(10)
test.add(15)
test.add(20)
test.add(17)
test.add(25)
test.add(30)
test.display()
print(test.peek())
test.poll()
test.display()
test.poll()
test.display()
