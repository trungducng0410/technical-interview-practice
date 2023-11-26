class Solution:
    # Time complexity: O(n*4^n)
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(comb, i):
            if len(comb) == len(digits):
                res.append("".join(comb))
                return

            for char in digitMap[digits[i]]:
                comb.append(char)

                backtrack(comb, i + 1)

                comb.pop()

        if digits:
            backtrack([], 0)
        return res


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitMap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(comb, i):
            if len(comb) == len(digits):
                res.append(comb)
                return

            for char in digitMap[digits[i]]:
                backtrack(comb + char, i + 1)

        if digits:
            backtrack("", 0)
        return res
