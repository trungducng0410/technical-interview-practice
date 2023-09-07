class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.capacity = 10
        self.map = [None] * self.capacity

    # O(1)
    def hash(self, value):
        return len(value) % len(self.map)

    # Time complexity:
    # Worst case: O(n) with collision
    # Normally: O(1)
    # Space complexity:
    # O(1)
    def setItem(self, key, value):
        index = self.hash(key)
        node = self.map[index]
        if node is None:
            self.map[index] = Node(key, value)  # type: ignore
            return
        prev = node
        while node is not None:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        prev.next = Node(key, value)

    # Time complexity:
    # Worst case: O(n) with collision
    # Normally: O(1)
    # Space complexity:
    # O(1)
    def getItem(self, key):
        index = self.hash(key)
        node = self.map[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        return None


hashMap = HashMap()
hashMap.setItem("Hello", "World")

print(hashMap.map)

item = hashMap.getItem("Hello")

print(item)

hashMap.setItem("Hello", "Duc")

item = hashMap.getItem("Hello")

print(item)

item = hashMap.getItem("Hihi")

print(item)
