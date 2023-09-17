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


# Time complexity: O(1)
# Space complexity: O(1)
def addFirst(head, node):
    if head == None:
        return node

    node.next = head
    return node


# Brute force
# Time complexity: O(n)
# Space complexity: O(n)
def partition(head, value):
    left = None
    right = None

    cur = head
    while cur != None:
        if cur.value < value:
            left = addFirst(left, Node(cur.value, None))
        else:
            right = addFirst(right, Node(cur.value, None))
        cur = cur.next

    cur = left
    while cur.next != None:
        cur = cur.next
    cur.next = right

    return left


# We can make it better than O(n) in time complexity, but we can optimize space complexity to O(1)
# Time complexity: O(n)
# Space complexity: O(1)
def partitionInplace(head, value):
    prev = head
    cur = head.next
    while cur != None:
        if cur.value < value:
            nextNode = cur.next

            # Make cur node as new head
            cur.next = head
            head = cur

            # remove cur node
            prev.next = nextNode
            cur = nextNode
        else:
            prev = prev.next
            cur = cur.next
    return head


test = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1, None)))))))
printList(test)
result = partition(test, 5)
printList(result)

test = Node(3, Node(1, Node(8, Node(5, Node(10, Node(2, Node(1, None)))))))
printList(test)
result = partitionInplace(test, 5)
printList(result)
