class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def findMaxSumSubArray(self, k, arr):
        maxSum = 0
        windowSum, windowStart = 0, 0
        for windowEnd in range(len(arr)):
            windowSum += arr[windowEnd]
            if windowEnd >= k - 1:
                maxSum = max(maxSum, windowSum)
                windowSum -= arr[windowStart]
                windowStart += 1
        return maxSum
