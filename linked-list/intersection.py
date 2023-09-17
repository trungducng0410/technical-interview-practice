# Brute force: Traverse through each node in first list, go through second list to see if any match
# Time complexity: O(a*b)
# Space complexity: O(1)
# We can also use hash table for first list then loop through second list
# Time complexity: O(a + b)
# Space complexity: O(a)


# If we connect last node of second list with head of first list => Become loop detection problem
# We can solve it in O(a + b) time and O(1) space

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


# Time complexity: O(a + b)
# Space complexity: O(1)
def findIntersect(head1, head2):
    len1 = length(head1)
    len2 = length(head2)
    if len1 > len2:
        head1 = moveNext(head1, len1 - len2)
    else:
        head2 = moveNext(head2, len2 - len1)

    while head1 != None and head2 != None:
        if head1 == head2:
            return head1

        head1 = head1.next
        head2 = head2.next

    return None


def length(head):
    i = 0
    while head != None:
        i += 1
        head = head.next
    return i


def moveNext(head, steps):
    for i in range(steps):
        if head != None:
            head = head.next
    return head


intersect = Node(6, Node(7, Node(8, None)))
head1 = Node(1, Node(2, intersect))
head2 = Node(3, Node(4, Node(5, intersect)))

print(findIntersect(head1, head2))
print(findIntersect(head1, head2).value)
print(findIntersect(Node(1, Node(2, Node(3, None))), Node(4, Node(5, Node(6, None)))))
