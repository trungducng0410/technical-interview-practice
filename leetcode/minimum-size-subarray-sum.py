class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = len(nums) + 1
        windowSum, start = 0, 0
        for end in range(len(nums)):
            windowSum += nums[end]
            while windowSum >= target:
                minLen = min(minLen, end - start + 1)
                windowSum -= nums[start]
                start += 1

        if minLen > len(nums):
            return 0

        return minLen
