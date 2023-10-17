class Solution:
    # Time: O(nlogn), Space: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, speed in sorted(zip(position, speed))[::-1]:
            time = (target - pos) / speed
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)


class Solution:
    # Time: O(nlogn), Space: O(1)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        longestTime = -1
        carFleet = 0
        for pos, speed in sorted(zip(position, speed))[::-1]:
            time = (target - pos) / speed
            if longestTime == -1 or time > longestTime:
                carFleet += 1
                longestTime = time

        return carFleet
