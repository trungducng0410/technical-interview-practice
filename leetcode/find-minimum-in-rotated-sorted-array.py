class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            m = (l + r) // 2

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m

        return nums[l]


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        curMin = nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                curMin = min(curMin, nums[l])
                break

            mid = (l + r) // 2
            curMin = min(curMin, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return curMin
