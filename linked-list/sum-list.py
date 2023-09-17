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
# Space complexity: O(1)
def sumLists(head1, head2):
    sum = 0
    i = 0
    while head1 != None:
        sum += (10 ** i) * head1.value
        head1 = head1.next
        i += 1

    j = 0
    while head2 != None:
        sum += (10 ** j) * head2.value
        head2 = head2.next
        j += 1

    return sum


head1 = Node(7, Node(1, Node(6, None)))
head2 = Node(5, Node(9, Node(2, None)))


# Time complexity: O(n)
# Space complexity: O(n)
def sumListsWithListReturned(head1, head2):
    remainder = 0
    dummy = Node(0, None)
    cur = dummy
    while head1 != None and head2 != None:
        val = remainder + head1.value + head2.value
        if val >= 10:
            val -= 10
            remainder = 1
        else:
            remainder = 0
        cur.next = Node(val, None)
        cur = cur.next
        head1 = head1.next
        head2 = head2.next

    while head1 != None:
        cur.next = Node(head1.value, None)
        cur = cur.next
        head1 = head1.next

    while head2 != None:
        cur.next = Node(head2.value, None)
        cur = cur.next
        head2 = head2.next

    if remainder > 0:
        cur.next = Node(remainder, None)

    return dummy.next


# Follow up: calculate if list is written in forward order
class PartialSum:
    def __init__(self, head, carry):
        self.head = head
        self.carry = carry


def sumListsInForwardOrder(head1, head2):
    if head1 == None and head2 == None:
        return None

    len1 = length(head1)
    len2 = length(head2)

    if len1 > len2:
        head2 = padList(head2, len1 - len2)
    elif len2 > len1:
        head1 = padList(head1, len2 - len1)

    result = addListsHelper(head1, head2)

    if result.carry > 0:
        res = addFirst(result.head, result.carry)
        return res

    return result.head


def length(head):
    i = 0
    while head != None:
        i += 1
        head = head.next
    return i


def padList(head, len):
    for i in range(len):
        head = addFirst(head, 0)
    return head


def addFirst(head, value):
    newHead = Node(value, None)
    newHead.next = head
    return newHead


def addListsHelper(node1, node2):
    if node1 == None and node2 == None:
        return PartialSum(None, 0)

    sum = addListsHelper(node1.next, node2.next)

    val = sum.carry + node1.value + node2.value

    head = addFirst(sum.head, val % 10)

    sum.head = head
    sum.carry = val // 10

    return sum


# print(sumLists(head1, head2))
# printList(sumListsWithListReturned(head1, head2))
# printList(sumListsWithListReturned(
#     Node(8, Node(7, Node(9, None))), Node(5, Node(8, Node(6, None)))))
printList(sumListsInForwardOrder(
    Node(6, Node(1, Node(7, None))), Node(2, Node(9, Node(5, Node(1, None))))))
