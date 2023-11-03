class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two = 0, len(nums) - 1

        i = 0
        while i < two:
            if i > zero and nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
            elif i < two and nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1
            else:
                i += 1
