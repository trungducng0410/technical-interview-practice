class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def checkIfPangram(self, sentence: str) -> bool:
        freqs = [0] * 26  # a - z

        for c in sentence:
            index = ord(c) - ord("a")
            freqs[index] += 1

        for freq in freqs:
            if freq == 0:
                return False

        return True
