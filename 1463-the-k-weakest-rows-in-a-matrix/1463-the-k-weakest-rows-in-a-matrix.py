class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldier_counts = []
    

        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                count += mat[i][j]
            soldier_counts.append((i, count))
        

        soldier_counts.sort(key=lambda x: (x[1], x[0]))
        

        weakest_rows = []
        for i in range(k):
            weakest_rows.append(soldier_counts[i][0])
        
        return weakest_rows