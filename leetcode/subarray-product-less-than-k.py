class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        res = 0
        left, right = 0, 0

        product = 1
        while right < len(nums):
            product *= nums[right]

            while product >= k and left < len(nums):
                product /= nums[left]
                left += 1

            res += right - left + 1

            right += 1

        return res
