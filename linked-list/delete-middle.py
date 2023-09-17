class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def printList(head):
    result = []
    while head != None:
        result.append(str(head.value))
        head = head.next
    print(" ".join(result))


midNode = Node(3, Node(4, Node(5, None)))
test = Node(1, Node(2, midNode))


# Time complexity: O(n)
# Space complexity: O(1)
def deleteMiddle(midNode):
    prev = midNode
    cur = midNode.next

    while cur.next != None:
        prev.value = cur.value
        prev = prev.next
        cur = cur.next

    prev.value = cur.value
    prev.next = None


# Time complexity: O(1)
# Space complexity: O(1)
def deleteNode(node):
    if node == None or node.next == None:
        return
    node.value = node.next.value
    node.next = node.next.next


midNode = Node(3, Node(4, Node(5, None)))
test = Node(1, Node(2, midNode))
printList(test)
deleteMiddle(midNode)
printList(test)


midNode = Node(3, Node(4, Node(5, None)))
test = Node(1, Node(2, midNode))
printList(test)
deleteNode(midNode)
printList(test)
