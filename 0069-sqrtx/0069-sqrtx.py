class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        for i in range(x + 1):
            isquared = i * i
            jsquared = (i + 1) * (i + 1)
            if isquared <= x < jsquared:
                return i