class Solution:
    # Time complexity: O(n*k) n: number of str, k: length of string
    # Space complexity: O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMaps = []
        for word in strs:
            charsMap = self.buildCharsMap(word)
            strMaps.append((charsMap, word))

        results = {}
        for item in strMaps:
            if item[0] in results:
                results[item[0]].append(item[1])
            else:
                results[item[0]] = [item[1]]

        return results.values()

    def buildCharsMap(self, word):
        charsMap = [0] * 26  # From a to z
        for char in word:
            # Map index to [0, 25]
            index = ord(char) - ord("a")
            charsMap[index] += 1

        return tuple(charsMap)

# Brute force: sort each string to be the key O(n * k * logk), space O(1)


class SolutionBruteForce:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            sortedWord = sorted(word)
            if sortedWord in results:
                results[sortedWord].append(word)
            else:
                results[sortedWord] = [word]
        return results.values()
