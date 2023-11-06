# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            while stack and node.val > stack[-1]:
                stack.pop()
            stack.append(node.val)
            node = node.next

        head = ListNode(stack[0])
        node = head
        for i in range(1, len(stack)):
            node.next = ListNode(stack[i])
            node = node.next

        return head


# Better solution - 1 pass
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(inf)
        stack = [dummy]
        node = head
        while node:
            while stack and node.val > stack[-1].val:
                stack.pop()
            stack[-1].next = node
            stack.append(node)
            node = node.next

        return dummy.next
