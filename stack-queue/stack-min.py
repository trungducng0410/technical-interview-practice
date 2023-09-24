class MinStack:
    def __init__(self):
        self.data = []

    def peek(self):
        if len(self.data) == 0:
            raise ValueError("Stack is empty")

        return self.data[-1][0]

    def push(self, value):
        if len(self.data) == 0:
            self.data.append([value, value])
        else:
            topItem = self.data[-1]
            currentMin = topItem[1]
            if currentMin > value:
                self.data.append([value, value])
            else:
                self.data.append([value, currentMin])

    def pop(self):
        if len(self.data) == 0:
            raise ValueError("Stack is empty")

        deleteItem = self.data.pop()
        return deleteItem[0]

    def getMin(self):
        if len(self.data) == 0:
            raise ValueError("Stack is empty")

        return self.data[-1][1]

    def display(self):
        print(self.data)
