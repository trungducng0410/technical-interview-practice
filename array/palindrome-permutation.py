# Brute force
# 1. Sort the string
# 2. Check pairs of characters
#   2.1. If len is even -> sliding window size 2, step 2
#   2.2. If len is odd -> every character has its pair, 1 character left
# Time complexity: O(nlogn)
# Space complexity: O(1)

# Question to ask:
# Is ASCII character? Yes
# Is space character included? No
# Is the string is case sensitive? No

# Time complexity: O(n)
# Space complexity: O(1) - 256 characters
def isPalindromePermutation(str):
    def buildCharsMap(str):
        charsMap = {}
        for char in str:
            if char == " ":
                continue

            if char in charsMap:
                charsMap[char] += 1
            else:
                charsMap[char] = 1
        return charsMap

    charsMap = buildCharsMap(str.lower())
    numOfOdd = 0
    for char in charsMap:
        if charsMap[char] % 2 != 0:
            numOfOdd += 1

    return numOfOdd <= 1


print(isPalindromePermutation("abcabc"))
print(isPalindromePermutation("abc"))
print(isPalindromePermutation("Tact Coa"))
