# Time complexity: O(n)
# Space complexity: O(n)
def toUrl(str):
    chars = []
    for char in str:
        if char == " ":
            chars.append("%")
            chars.append("2")
            chars.append("0")
        else:
            chars.append(char)
    return "".join(chars)


# Time complexity: O(n)
# Space complexity: O(n)
def toUrlInplace(str):
    chars = [char for char in str]
    for i in range(len(chars)):
        if chars[i] == " ":
            chars[i] = "%20"
    return "".join(chars)


# Time complexity: O(n)
# Space complexity: O(1)
def toUrlArray(str, length):
    def countSpaces(str):
        count = 0
        for char in str:
            if char == " ":
                count += 1
        return count

    numOfSpaces = countSpaces(str)
    newLength = length + numOfSpaces * 2

    # Not count to space complexity if it's input
    chars = ["" for i in range(newLength)]

    for i in range(length - 1, -1, -1):
        if str[i] != " ":
            chars[newLength - 1] = str[i]
            newLength = newLength - 1
        else:
            chars[newLength - 1] = "0"
            chars[newLength - 2] = "2"
            chars[newLength - 3] = "%"
            newLength = newLength - 3

    return "".join(chars)


print(toUrl("Mr John Smith"))
print(toUrlInplace("Mr John Smith"))
print(toUrlArray("Mr John Smith", 13))

# Trick: Loop from the end to modify string without the need to shift the array
