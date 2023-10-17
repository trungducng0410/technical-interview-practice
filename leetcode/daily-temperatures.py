class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                topIndex = stack.pop()
                res[topIndex] = i - topIndex
            stack.append(i)

        return res

# Tip: Monotonic stack - Time: O(n), Space: O(n)
# Brute force: Time: O(n^2), Space: O(1)
