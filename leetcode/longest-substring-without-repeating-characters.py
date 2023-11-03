class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        chars = set()
        for r in range(len(s)):
            while l < r and s[r] in chars:
                chars.remove(s[l])
                l += 1

            maxLength = max(maxLength, r - l + 1)
            chars.add(s[r])
            r += 1

        return maxLength
