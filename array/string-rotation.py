def isSubString(subString, baseString):
    return subString in baseString


# Brute force
# Time complexity: O(n^2)
# Space complexity: O(1)
def isStringRotationBruteForce(str1, str2):
    for i in range(len(str2) - 1):
        subStr1 = str2[:i + 1]
        subStr2 = str2[i + 1:]
        if isSubString(subStr1, str1) and isSubString(subStr2, str1):
            return True
    return False


# Optimal solution
# Time complexity: O(n)
# Space complexity: O(1)
def isStringRotation(str1, str2):
    if len(str1) != len(str2):
        return False

    return isSubString(str2, str1 + str1)


# "waterbottle", "erbottlewat"
# "wat" - x, "erbottle" - y => str1: xy, str2: yx => str2 (yx) will be substring of str1str2 (xyxy)
# "waterbottlewaterbottle"
# Rotated string can divide into 2 parts that are both substring of original string


print(isStringRotation("waterbottle", "erbottlewat"))
print(isStringRotationBruteForce("waterbottle", "erbottlewat"))
