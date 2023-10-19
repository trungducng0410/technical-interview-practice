class Solution:
    # Time complexity: O(n), Space complexity: O(1)
    # Trick: start with widest then try to move shorter edge
    def maxArea(self, height: List[int]) -> int:
        res = 0
        start, end = 0, len(height) - 1

        while start < end:
            curArea = min(height[start], height[end]) * (end - start)
            res = max(res, curArea)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return res
