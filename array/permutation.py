# Questions
# What is permutation? abcd and adcb, acdb

# Brute force
# Generate all permutation and compare it with other string
# Slow, hard to implement...

# Time complexity: O(nlogn)
# Space complexity: O(n)
def checkIfPermutationWithSort(str1, str2):
    if len(str1) != len(str2):
        return False

    sortedStr1 = "".join(sorted(str1))
    sortedStr2 = "".join(sorted(str2))

    return sortedStr1 == sortedStr2


# Time complexity: O(n)
# Space complexity: O(1)
def checkIfPermutationWithHashMap(str1, str2):
    # Key - character, value - number of existence
    def buildCharMap(str):
        charMap = {}
        for char in str:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        return charMap

    if len(str1) != len(str2):
        return False

    str1Map = buildCharMap(str1)
    str2Map = buildCharMap(str2)

    if len(str1Map) != len(str2Map):
        return False

    for key in str1Map:
        if key not in str2Map:
            return False

        if str1Map[key] != str2Map[key]:
            return False

        str2Map.pop(key)

    if len(str2Map) > 0:
        return False

    return True


# Optimal solution
# Time complexity: O(n)
# Space complexity: O(1)
def checkIfPermutationWithOneHashMap(str1, str2):
    # Key - character, value - number of existence
    def buildCharMap(str):
        charMap = {}
        for char in str:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        return charMap

    if len(str1) != len(str2):
        return False

    str1Map = buildCharMap(str1)

    for char in str2:
        if char not in str1Map:
            return False
        str1Map[char] -= 1

    for key in str1Map:
        if str1Map[key] != 0:
            return False

    return True


print(checkIfPermutationWithSort("abcd", "acbd"))
print(checkIfPermutationWithSort("abcd", "aaaa"))
print(checkIfPermutationWithSort("abcd", "abcde"))
print(checkIfPermutationWithSort("abcd", "acdf"))
print(checkIfPermutationWithHashMap("abcd", "acbd"))
print(checkIfPermutationWithHashMap("abcd", "aaaa"))
print(checkIfPermutationWithHashMap("abcd", "abcde"))
print(checkIfPermutationWithHashMap("abcd", "acdf"))
print(checkIfPermutationWithOneHashMap("abcd", "acbd"))
print(checkIfPermutationWithOneHashMap("abcd", "aaaa"))
print(checkIfPermutationWithOneHashMap("abcd", "abcde"))
print(checkIfPermutationWithOneHashMap("abcd", "acdf"))
