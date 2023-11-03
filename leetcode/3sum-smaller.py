class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def searchTriplets(self, arr, target):
        count = 0
        arr.sort()

        for i in range(len(arr) - 2):
            left, right = i + 1, len(arr) - 1
            while left < right:
                curSum = arr[i] + arr[left] + arr[right]

                if curSum >= target:
                    right -= 1
                else:
                    count += right - left
                    left += 1

        return count
