class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        
        trust_count = []
        for i in range(n + 1):
            trust_count.append(0)

        
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
    
        return -1
