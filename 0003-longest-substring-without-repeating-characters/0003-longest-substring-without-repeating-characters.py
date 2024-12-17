class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlength = 0
        seen = set()
        
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[i])
            maxlength = max(maxlength, i - start + 1)
        
        return maxlength
