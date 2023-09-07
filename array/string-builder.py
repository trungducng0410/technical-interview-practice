class ArrayList:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    # Worst case: O(n) when resize array
    # O(1)
    def add(self, value):
        if self.size < self.capacity:
            index = self.size
            self.arr[index] = value
            self.size += 1
        else:
            # Resize array
            self.capacity = self.capacity * 2
            newArr = [None] * self.capacity

            # Copy values from old array to new one
            for index in range(len(self.arr)):
                newArr[index] = self.arr[index]

            newArr[self.size] = value
            self.arr = newArr
            self.size += 1


class StringBuilder:
    def __init__(self):
        self.characters = ArrayList()

    # O(n) - n is the length of word
    def append(self, word):
        for char in word:
            self.characters.add(char)

    # O(n) - n is number of characters
    def toString(self):
        res = ""
        for char in self.characters.arr:
            if char is None:
                break
            res += char
        return res


sentence = StringBuilder()

sentence.append("Hello")

print(sentence.toString())

sentence.append(" World")

print(sentence.toString())
