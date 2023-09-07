# What to confirm?
# 1. Is ASCII or Unicode?
# 2. Can you additional data structure to solve?

# Time complexity: O(n^2)
# Space complexity: O(1)
def isUniqueCharsWithNestedLoop(str):
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False

    return True


# Optimal solution
# Time complexity: O(n)
# Space complexity: O(1) - only have upto 256 characters
def isUniqueCharsWithHashMap(str):
    charSet = set()
    for char in str:
        if char in charSet:
            return False
        else:
            charSet.add(char)

    return True


# Time complexity: O(nlogn)
# Space complexity: O(n) - n is the length of the string
def isUniqueCharsWithSort(str):
    chars = [char for char in str]
    chars.sort()
    for i in range(len(str) - 1):
        if chars[i] == chars[i + 1]:
            return False
    return True


print(isUniqueCharsWithNestedLoop("abcde"))
print(isUniqueCharsWithNestedLoop("abcda"))
print(isUniqueCharsWithNestedLoop("aaaaa"))
print(isUniqueCharsWithHashMap("abcde"))
print(isUniqueCharsWithHashMap("abcda"))
print(isUniqueCharsWithHashMap("aaaaa"))
print(isUniqueCharsWithSort("abcde"))
print(isUniqueCharsWithSort("abcda"))
print(isUniqueCharsWithSort("aaaaa"))
