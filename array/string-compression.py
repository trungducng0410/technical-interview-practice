# Time complexity: O(n)
# Space complexity: O(n)
def compressString(string):
    # Additional check to avoid unnecessary string
    if len(string) <= countCompressLength(string):
        return string

    compressedChars = []
    for char in string:
        if len(compressedChars) == 0:
            compressedChars.append(char)
            compressedChars.append(1)
            continue

        if compressedChars[len(compressedChars) - 2] == char:
            compressedChars[len(compressedChars) - 1] += 1
        else:
            compressedChars.append(char)
            compressedChars.append(1)

    for i in range(len(compressedChars)):
        compressedChars[i] = str(compressedChars[i])

    compressedStr = "".join(compressedChars)

    return compressedStr


# Time complexity: O(n)
# Space complexity: O(1)
def countCompressLength(string):
    newLength = 0
    countConsecutive = 1
    for i in range(len(string)):
        countConsecutive += 1
        if i + 1 >= len(string) or string[i] != string[i + 1]:
            newLength = newLength + 1 + len(str(countConsecutive))
            countConsecutive = 1

    return newLength


print(compressString("aaabcdefgh"))
print(compressString("aabcccccaaa"))
