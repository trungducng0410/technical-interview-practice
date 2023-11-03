# Brute force solution
# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i * i <= x:
            i += 1

        return i - 1


# Optimal solution using binary search
# Time complexity: O(logn)
# Space complexity: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            if x < num:
                right = mid - 1
            elif x > num:
                left = mid + 1
            else:
                return mid

        return right
