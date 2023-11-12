# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        while node:
            nextHead = node.next
            node.next = self.reverseList(nextHead)
            node = node.next

        return head

    def reverseList(self, head):
        if not head:
            return None

        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head:
            nodes.append(head)

        dummy = ListNode()
        node = dummy
        left, right = 0, len(nodes) - 1
        while left < right:
            node.next = left
            node = node.next
            left += 1

            node.next = right
            node = node.next
            right -= 1

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow, dummy = head, head, ListNode(0, head)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            dummy = dummy.next

        dummy.next = None
        slow = self.reverseList(slow)

        left, right = head, slow

        if left == right:
            return head

        dummy = ListNode()
        node = dummy
        while left and right:
            nextLeft = left.next
            node.next = left
            node = node.next
            left = nextLeft

            nextRight = right.next
            node.next = right
            node = node.next
            right = nextRight

        return dummy.next

    def reverseList(self, head):
        if not head:
            return None

        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow, dummy = head, head, ListNode(0, head)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None
        second = self.reverseList(second)

        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head

    def reverseList(self, head):
        if not head:
            return None

        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode

        return prev
