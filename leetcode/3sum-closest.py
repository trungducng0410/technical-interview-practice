class Solution:
    # Time complexity: O(n^2)
    # Space complexity: O(1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closestSum = None

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                curSum = nums[i] + nums[left] + nums[right]

                if closestSum == None:
                    closestSum = curSum

                if abs(target - curSum) < abs(target - closestSum):
                    closestSum = curSum

                if curSum < target:
                    left += 1
                elif curSum > target:
                    right -= 1
                else:
                    return curSum

        return closestSum
