class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char)
        charsstr = ''.join(chars)
        return chars == chars[::-1]