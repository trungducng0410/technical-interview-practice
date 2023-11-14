# Brute force solution
# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniqNums = set()
        for n in nums:
            if n in uniqNums:
                return n

            uniqNums.add(n)


# Time complexity: O(n)
# Space complexity: O(1)
# Modified the input
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        while True:
            if nums[0] == nums[nums[0]]:
                return nums[0]

            j = nums[0]
            nums[0], nums[j] = nums[j], nums[0]


# Time complexity: O(n)
# Space complexity: O(1)
# Not modified input, linked list cycle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
