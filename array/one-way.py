# Time complexity: O(n)
# Space complexity: O(1)
def checkOneWay(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    s1, s2 = str1, str2
    if len(str1) < len(str2):
        s1, s2 = s2, s1

    foundDifference = False
    i = 0
    j = 0

    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if foundDifference:
                return False
            foundDifference = True

            if len(s1) != len(s2):
                i += 1
        i += 1
        j += 1

    return True


# Time complexity: O(n)
# Space complexity: O(1)
def checkOneWayWithSeparateSteps(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        return checkCanReplace(str1, str2)
    elif len(str1) > len(str2):
        return checkCanInsert(str1, str2)
    else:
        return checkCanInsert(str2, str1)


def checkCanReplace(str1, str2):
    foundDifference = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if foundDifference:
                return False
            foundDifference = True

    return True


def checkCanInsert(str1, str2):
    foundDifference = False
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if foundDifference:
                return False
            foundDifference = True
            i += 1

        i += 1
        j += 1

    return True


print(checkOneWay("pale", "ple"))
print(checkOneWay("pales", "pale"))
print(checkOneWay("pale", "bale"))
print(checkOneWay("pble", "bale"))
print(checkOneWay("pale", "bake"))

print(checkOneWayWithSeparateSteps("pale", "ple"))
print(checkOneWayWithSeparateSteps("pales", "pale"))
print(checkOneWayWithSeparateSteps("pale", "bale"))
print(checkOneWayWithSeparateSteps("pble", "bale"))
print(checkOneWayWithSeparateSteps("pale", "bake"))
