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


# Time complexity: O(n)
# Space complexity: O(n)
def removeDuplicates(head):
    uniqValues = set()
    node = head
    prev = Node(None, head)
    while node != None:
        if node.value in uniqValues:
            nextNode = node.next
            prev.next = nextNode
        else:
            uniqValues.add(node.value)
            prev = prev.next

        node = node.next

    return head


# Time complexity: O(n^2)
# Space complexity: O(1)
def removeDuplicatesWithoutBuffer(head):
    node = head

    while node != None:
        prev = node
        cur = node.next
        while cur != None:
            if cur.value == node.value:
                nextNode = cur.next
                prev.next = nextNode
            else:
                prev = prev.next

            cur = cur.next

        node = node.next

    return head


test = Node(1, Node(2, Node(2, Node(4, Node(5, Node(4, None))))))
printList(test)

uniqList = removeDuplicates(test)
printList(uniqList)

test1 = Node(1, Node(2, Node(2, Node(4, Node(5, Node(4, Node(4, None)))))))
printList(test1)

uniqList1 = removeDuplicatesWithoutBuffer(test1)
printList(uniqList1)
