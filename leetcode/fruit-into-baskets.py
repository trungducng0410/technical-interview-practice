class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        count = {}
        start = 0

        for end in range(len(fruits)):
            count[fruits[end]] = 1 + count.get(fruits[end], 0)

            while len(count) > 2:
                startFruit = fruits[start]
                count[startFruit] -= 1
                if count[startFruit] == 0:
                    del count[startFruit]
                start += 1

            maxFruits = max(maxFruits, end - start + 1)

        return maxFruits
