import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time complexity: O(n), Space complexity: O(1)

        # O(n)
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        # O(n / 2) = O(n)
        for i in range(len(cleaned_string) // 2):
            j = len(cleaned_string) - 1 - i
            if cleaned_string[i] != cleaned_string[j]:
                return False

        return True
