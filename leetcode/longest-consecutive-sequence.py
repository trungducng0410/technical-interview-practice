class Solution:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(nlogn)
        sortedUniqNums = sorted(list(set(nums)))

        n = len(sortedUniqNums)
        if n == 0 or n == 1:
            return n

        longestSequence = 1
        currSequence = 1
        for i in range(n - 1):
            if sortedUniqNums[i + 1] - sortedUniqNums[i] == 1:
                currSequence += 1
                continue
            else:
                longestSequence = max(longestSequence, currSequence)
                currSequence = 1

        return max(longestSequence, currSequence)


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longestSequence = 0
        # It looks like nested loops but we actually run through each sequence once (only start when find the first element in sequence) => O(n)
        for num in nums:
            # check if its the start of a sequence
            if num - 1 not in nums:
                start = num
                currSequence = 1
                while start + 1 in nums:
                    currSequence += 1
                    start += 1
                longestSequence = max(longestSequence, currSequence)

        return longestSequence
