from collections import Counter

# Brute force solution: Nested for loop - O(n^2)


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numCount = Counter(nums)
        res = 0
        for value in numCount.values():
            res += (value * (value - 1)) // 2
        return res


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count = {}
        for num in nums:
            if num in count:
                res += count[num]
                count[num] += 1
            else:
                count[num] = 1

        return res
