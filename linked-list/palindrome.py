# Brute force: convert to array and use 2 pointers (Time complexity: O(n), space complexity: O(n))
# If doubly linked list, same as arrays (Time complexity: O(n), space complexity: O(1))


# We will solve the problem with singly linked list

# a b c d c b a -> a b c | a b c (split into 2 list, reverse second list then use 2 pointers)
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


def length(node):
    i = 0
    while node != None:
        i += 1
        node = node.next
    return i


def splitList(head, len):
    firstHead = head
    secondHead = None

    node = head
    for i in range(len // 2):
        node = node.next
    secondHead = node

    return firstHead, secondHead


def addFirst(head, value):
    newHead = Node(value, None)
    newHead.next = head
    return newHead


def reverseList(head):
    newHead = None
    while head != None:
        newHead = addFirst(newHead, head.value)
        head = head.next
    return newHead


# Time complexity: O(n)
# Space complexity: O(1) if reverse in-place
def isPalindrome(head):
    if head == None:
        return True

    len = length(head)

    head1, head2 = splitList(head, len)

    reversedHead2 = reverseList(head2)

    while head1 != None and reversedHead2 != None:
        if head1.value != reversedHead2.value:
            return False
        head1 = head1.next
        reversedHead2 = reversedHead2.next

    return True


# Time complexity: O(n)
# Space complexity: O(n)
def isPalindromeWithStack(head):
    stack = []
    slow = head
    fast = head
    while fast != None and fast.next != None:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    # If len is odd, skip middle node
    if fast != None:
        slow = slow.next

    while slow != None:
        val = stack.pop()
        if slow.value != val:
            return False
        slow = slow.next

    return len(stack) == 0


test = Node(1, Node(2, Node(3, Node(2, Node(1, None)))))
print(isPalindrome(test))
print(isPalindromeWithStack(test))

test2 = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1, None))))))
print(isPalindrome(test2))
print(isPalindromeWithStack(test2))

test2 = Node(1, Node(2, Node(3, Node(3, Node(2, Node(1, Node(4, None)))))))
print(isPalindrome(test2))
print(isPalindromeWithStack(test2))
