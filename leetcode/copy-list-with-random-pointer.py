"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = Node(-1)
        cur = dummy
        indexes = {}

        i = 0
        node = head
        while node:
            indexes[node] = i
            cur.next = Node(node.val)
            node = node.next
            cur = cur.next
            i += 1

        cur = dummy.next
        node = head
        while cur and node:
            randomNode = node.random

            if randomNode == None:
                cur.random = None
            else:
                index = indexes[randomNode]
                tmp = dummy.next
                for i in range(index):
                    tmp = tmp.next
                cur.random = tmp

            cur = cur.next
            node = node.next

        return dummy.next


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            nextNode = cur.next
            cur.next = Node(cur.val)
            cur.next.next = nextNode
            cur = nextNode

        cur = head
        while cur:
            randomNode = cur.random
            if randomNode:
                cur.next.random = randomNode.next
            else:
                cur.next.random = None

            cur = cur.next.next

        dummy = Node(1)
        cur = head
        node = dummy
        while cur:
            nextNode = cur.next
            node.next = nextNode
            cur = cur.next.next
            node = node.next

        return dummy.next


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            newNext = oldToCopy[cur.next]
            newRandom = oldToCopy[cur.random]

            copy.next = newNext
            copy.random = newRandom

            cur = cur.next

        return oldToCopy[head]
