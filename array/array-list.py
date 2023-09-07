class ArrayList:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.arr = [None] * self.capacity

    # Time complexity:
    # Worst case: O(n) when resize array
    # O(1)
    # Space complexity:
    # O(n)
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


arr = ArrayList()
arr.add(1)
print(arr.arr, arr.size, arr.capacity)
arr.add(2)
print(arr.arr, arr.size, arr.capacity)
arr.add(3)
print(arr.arr, arr.size, arr.capacity)
arr.add(4)
print(arr.arr, arr.size, arr.capacity)
arr.add(5)
print(arr.arr, arr.size, arr.capacity)
