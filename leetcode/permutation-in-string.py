from collections import defaultdict


class Solution:
    # Time complexity: O(26 * n)
    # Space complexity: O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # Compute freq of s1
        freqS1 = defaultdict(int)
        for c in s1:
            freqS1[c] += 1

        freq = defaultdict(int)
        left, right = 0, len(s1) - 1

        # Compute freq of substring in s2
        for i in range(left, right + 1):
            freq[s2[i]] += 1

        while right < len(s2):
            if self.compareDict(freqS1, freq) == True:
                return True

            if right == len(s2) - 1:
                return False

            removedChar = s2[left]
            addedChar = s2[right + 1]
            freq[removedChar] -= 1
            freq[addedChar] += 1
            left += 1
            right += 1

        return False

    def compareDict(self, dict1, dict2):
        for key in dict1:
            if dict1[key] != dict2[key]:
                return False

        return True


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26
