class SetOfStacks:
    def __init__(self, capacity):
        self.data = []
        self.capacity = capacity

    def pop(self):
        if len(self.data) == 0:
            raise ValueError("Stack is empty")

        topStack = self.data[-1]
        poppedValue = topStack.pop()
        if len(topStack) == 0:
            self.data.pop()

        return poppedValue

    def push(self, value):
        if len(self.data) == 0:
            newStack = [value]
            self.data.append(newStack)
        else:
            topStack = self.data[-1]
            if len(topStack) == self.capacity:
                newStack = [value]
                self.data.append(newStack)
            else:
                topStack.append(value)

    def peek(self):
        if len(self.data) == 0:
            raise ValueError("Stack is empty")

        return self.data[-1][-1]

    def display(self):
        print(self.data)
