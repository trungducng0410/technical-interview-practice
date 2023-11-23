class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(subset, nums):
            if not nums:
                res.append(subset[:])
                return

            for i in range(len(nums)):
                subset.append(nums[i])
                usedNum = nums.pop(i)

                backtrack(subset, nums)

                subset.pop()
                nums.insert(i, usedNum)

        backtrack([], nums)
        return res
