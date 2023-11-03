class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverseVowels(self, s: str) -> str:
        vowelsSet = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])

        vowels = []
        for c in s:
            if c in vowelsSet:
                vowels.append(c)

        result = []
        i = len(vowels) - 1

        for c in s:
            if c in vowelsSet:
                result.append(vowels[i])
                i -= 1
            else:
                result.append(c)

        return "".join(result)
