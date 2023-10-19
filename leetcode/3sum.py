class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(1)
    # If I write twoSum as different func and return pairs that sum to target, space complexity will increase to O(n).
    # I can write twoSum as a closure to reduce space complexity to O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # Skip duplicate target
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            target = -nums[i]

            # Find two some pairs
            start, end = i + 1, len(nums) - 1
            while start < end:
                curSum = nums[start] + nums[end]

                if curSum < target:
                    start += 1
                elif curSum > target:
                    end -= 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    # Find new unique numbers
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1

        return res
