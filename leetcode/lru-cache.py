# Definition for singly-linked list.
class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        # left: LRU, right: most recent
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from the list
    def remove(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next, nextNode.prev = nextNode, prevNode

    # Insert at right
    def insert(self, node):
        tail = self.right.prev

        self.right.prev = node
        tail.next = node
        node.next = self.right
        node.prev = tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
