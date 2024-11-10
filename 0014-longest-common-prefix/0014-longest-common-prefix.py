class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = strs[0]
        
        for string in strs[1:]:
            while string.find(pre) != 0:
                pre = pre[:-1]
                if pre == "":
                    return ""
        
        return pre
        