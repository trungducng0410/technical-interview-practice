class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = self.buildCharMap(s)
        tMap = self.buildCharMap(t)
        return self.isEqualMap(sMap, tMap)

    def buildCharMap(self, s):
        charMap = {}
        for c in s:
            if c in charMap:
                charMap[c] += 1
            else:
                charMap[c] = 1
        return charMap

    def isEqualMap(self, map1, map2):
        for item in map1:
            if item not in map2:
                return False

            if map1[item] != map2[item]:
                return False

        return True
