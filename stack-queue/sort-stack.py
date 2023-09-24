class SortedStack:
    def __init__(self):
        self.data = []

    # O(1)
    def peek(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")

        return self.data[-1]

    # O(1)
    def isEmpty(self):
        return len(self.data) == 0

    # O(n)
    def push(self, value):
        if self.isEmpty():
            self.data.append(value)
            return

        tmpStack = []
        while not self.isEmpty() and value >= self.data[-1]:
            valueAtTop = self.data.pop()
            tmpStack.append(valueAtTop)

        self.data.append(value)

        while len(tmpStack) != 0:
            valueAtTop = tmpStack.pop()
            self.data.append(valueAtTop)

    # O(1)
    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")

        deletedValue = self.data.pop()
        return deletedValue

    def display(self):
        print(self.data)


class Stack:
    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop()

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data[-1]

    def isEmpty(self):
        return len(self.data) == 0

    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def sort(self):
        tmp = []

        while not self.isEmpty():
            top = self.pop()
            while len(tmp) != 0 and tmp[-1] >= top:
                self.push(tmp.pop())
            tmp.append(top)

        while len(tmp) != 0:
            self.push(tmp.pop())

    def display(self):
        print(self.data)
