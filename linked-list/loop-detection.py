class NodeWithFlag:
    def __init__(self, value, next):
        self.value = value
        self.next = next
        self.visited = False


node1 = NodeWithFlag(1, None)
node2 = NodeWithFlag(2, None)
node3 = NodeWithFlag(3, None)
node4 = NodeWithFlag(4, None)
node5 = NodeWithFlag(5, None)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3


# Time complexity: O(n)
# Space complexity: O(1)
def detectLoopWithFlag(head):
    while head != None:
        if head.visited == True:
            return head
        head.visited = True
        head = head.next

    return None


print(detectLoopWithFlag(node1))
print(detectLoopWithFlag(NodeWithFlag(1, NodeWithFlag(
    2, NodeWithFlag(3, NodeWithFlag(4, None))))))


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


# Time complexity: O(n)
# Space complexity: O(1)
def detectLoop(head):
    slow = head
    fast = head

    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if fast == None or fast.next == None:
        return None

    slow = head
    while fast != None:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            return slow

    return None


print(detectLoop(node1))
print(detectLoop(NodeWithFlag(1, NodeWithFlag(
    2, NodeWithFlag(3, NodeWithFlag(4, None))))))
