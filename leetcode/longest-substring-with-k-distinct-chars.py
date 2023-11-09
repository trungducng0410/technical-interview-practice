class Solution:
    def findLength(self, str1, k):
        max_length = 0
        count = {}
        start = 0
        for end in range(len(str1)):
            count[str1[end]] = 1 + count.get(str1[end], 0)

            while len(count) > k and start < end:
                count[str1[start]] -= 1
                if count[str1[start]] == 0:
                    del count[str1[start]]
                start += 1

            max_length = max(max_length, end - start + 1)
        return max_length
