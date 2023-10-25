import math


class Solution:
    # Time complexity: O(log(m) * n) - m is the maximum pile, n is number of pile
    # Space complexity: O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        leftSpeed, rightSpeed = 1, max(piles)
        res = rightSpeed

        while leftSpeed <= rightSpeed:
            midSpeed = (leftSpeed + rightSpeed) // 2
            timeMid = self.timeToEat(piles, midSpeed)

            if h >= timeMid:
                res = midSpeed
                rightSpeed = midSpeed - 1
            else:
                leftSpeed = midSpeed + 1

        return res

    # Time complexity: O(n)
    # Space complexity: O(1)
    def timeToEat(self, piles, speed):
        time = 0
        for pile in piles:
            time += math.ceil(float(pile) / speed)
        return time
