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


# Brute force: Loop through the list to count the length -> Calculate index of k to the last element -> Loop again to find element
# Time complexity: O(n)
# Space complexity: O(1)
# We can't optimize the time complexity and the space complexity, but we can find it in one pass
def kToTheLastBruteForce(head, k):
    length = 0
    cur = head
    while cur != None:
        length += 1
        cur = cur.next

    index = length - 1 - k

    if index < 0:
        return None

    cur = head
    for i in range(index):
        cur = cur.next

    return cur.value


# Time complexity: O(n)
# Space complexity: O(1)
def kToTheLast(head, k):
    fast = head
    for i in range(k+1):
        if fast == None:
            return None
        fast = fast.next
    slow = head
    while fast != None:
        fast = fast.next
        slow = slow.next

    return slow.value


# Time complexity: O(n)
# Space complexity: O(n)
def kToTheLastRecursive(head, k):
    if head == None:
        return 0, head

    index, cur = kToTheLastRecursive(head.next, k)
    if index == k:
        return index + 1, head

    return index + 1, cur


test = Node(1, Node(2, Node(2, Node(4, Node(5, Node(4, None))))))
printList(test)

print(kToTheLastBruteForce(test, 1))
print(kToTheLastBruteForce(test, 0))
print(kToTheLastBruteForce(test, 3))

print(kToTheLast(test, 1))
print(kToTheLast(test, 0))
print(kToTheLast(test, 3))

i, res = kToTheLastRecursive(test, 1)
print(res.value)
i, res = kToTheLastRecursive(test, 0)
print(res.value)
i, res = kToTheLastRecursive(test, 3)
print(res.value)
