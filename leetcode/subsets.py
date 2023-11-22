class Solution:
    # Time complexity: O(n*2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # decision to exclude nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        self.backtrack(0, res, subset, nums)
        return res

    def backtrack(self, index, res, subset, nums):
        res.append(list(subset))

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.backtrack(i + 1, res, subset, nums)
            subset.pop()
