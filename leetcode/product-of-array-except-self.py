# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProducts = self.calculatePrefixProducts(nums)
        suffixProducts = self.calculateSuffixProducts(nums)

        results = []

        for i in range(n):
            productExceptSelf = prefixProducts[i] * suffixProducts[n - 1 - i]
            results.append(productExceptSelf)

        return results

    def calculatePrefixProducts(self, nums):
        prefixProducts = [1]
        for i in range(len(nums) - 1):
            lastProduct = prefixProducts[-1]
            accumulativeProduct = lastProduct * nums[i]
            prefixProducts.append(accumulativeProduct)
        return prefixProducts

    def calculateSuffixProducts(self, nums):
        suffixProducts = [1]
        for i in range(len(nums) - 1, 0, -1):
            lastProduct = suffixProducts[-1]
            accumulativeProduct = lastProduct * nums[i]
            suffixProducts.append(accumulativeProduct)
        return suffixProducts


# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        results = [1] * n
        prefix = 1
        for i in range(n):
            results[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            results[i] *= postfix
            postfix *= nums[i]

        return results
