class Solution:
    # Using 2 pointers
    # Time complexity: O(n), Space complexity: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
