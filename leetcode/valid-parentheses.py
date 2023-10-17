class Solution:
    def isValid(self, s: str) -> bool:
        parenthesesMap = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        stack = []

        for c in s:
            if c in parenthesesMap:
                stack.append(c)
                continue

            if len(stack) == 0 or parenthesesMap[stack[-1]] != c:
                return False

            stack.pop()

        return len(stack) == 0
