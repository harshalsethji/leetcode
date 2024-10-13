class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split()
        lenth = len(split)
        
        lastword = split[lenth-1]
        lastlegnth = len(lastword)
        return lastlegnth