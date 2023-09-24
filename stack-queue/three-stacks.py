# 0 1 2 3 4 5

class ThreeStacks:
    def __init__(self, stackCap):
        dataCap = stackCap * 3
        self.data = [None] * dataCap
        self.start = [0, dataCap // 3, 2 * (dataCap // 3)]
        self.end = [dataCap // 3, 2 * (dataCap // 3), dataCap]

    # Time complexity: O(1)
    def peek(self, stackNum):
        if stackNum > 2:
            raise ValueError(f"Stack {stackNum} is not exist")
        top = self.start[stackNum] - 1
        if top < 0 or self.data[top] == None:
            raise ValueError(f"Stack {stackNum} is empty. Cannot peek")

        return self.data[top]

    # Time complexity: O(1)
    def push(self, stackNum, value):
        if stackNum > 2:
            raise ValueError(f"Stack {stackNum} is not exist")
        if self.start[stackNum] >= self.end[stackNum]:
            raise ValueError(f"Stack {stackNum} is full")

        self.data[self.start[stackNum]] = value
        self.start[stackNum] += 1

    # Time complexity: O(1)
    def pop(self, stackNum):
        if stackNum > 2:
            raise ValueError(f"Stack {stackNum} is not exist")
        top = self.start[stackNum] - 1
        if top < 0 or self.data[top] == None:
            raise ValueError(f"Stack {stackNum} is empty")

        value = self.data[top]

        self.data[top] = None
        self.start[stackNum] -= 1

        return value

    def display(self):
        print(self.data)
