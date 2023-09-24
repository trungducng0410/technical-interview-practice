class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # Time complexity: O(1)
    def add(self, value):
        self.stack1.append(value)

    # Time complexity: O(n)
    def remove(self):
        if len(self.stack1) == 0:
            raise ValueError("Queue is empty")

        self.transferItems(self.stack1, self.stack2)

        deletedValue = self.stack2.pop()

        self.transferItems(self.stack2, self.stack1)

        return deletedValue

    # Time complexity: O(1)
    def peek(self):
        if len(self.stack1) == 0:
            raise ValueError("Queue is empty")

        return self.stack1[0]

    # Time complexity: O(1)
    def isEmpty(self):
        return len(self.stack1) == 0

    def transferItems(self, fromStack, toStack):
        for i in range(len(fromStack)):
            toStack.append(fromStack.pop())

    def display(self):
        print(self.stack1)
