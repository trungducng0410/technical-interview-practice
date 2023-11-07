class Solution:
    # Time complexity: O(n*k)
    # Space complexity: O(n)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if self.isAdjacentDuplicates(stack, k, c):
                for i in range(k - 1):
                    stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    def isAdjacentDuplicates(self, chars, k, cur):
        if len(chars) < k - 1:
            return False

        for i in range(k - 1):
            if chars[len(chars) - 1 - i] != cur:
                return False

        return True


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack.append((c, stack[-1][1] + 1))
            else:
                stack.append((c, 1))

            if stack and stack[-1][1] == k:
                for i in range(k):
                    stack.pop()

        return "".join([pair[0] for pair in stack])


# Don't need a loop to pop items
class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])

            if stack and stack[-1][1] == k:
                stack.pop()

        return "".join([c * n for c, n in stack])
