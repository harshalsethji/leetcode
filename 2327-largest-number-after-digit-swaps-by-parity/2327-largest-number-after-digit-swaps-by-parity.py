class Solution:
    def largestInteger(self, num: int) -> int:
        digits = []
        for d in str(num):
            digits.append(int(d))
        
        even_digits = []
        odd_digits = []
        for d in digits:
            if d%2 == 0:
                even_digits.append(d)
            else:
                odd_digits.append(d)
        even_digits.sort(reverse = True)
        odd_digits.sort(reverse = True)

        result = []
        even = 0
        odd = 0

        for d in digits:
            if d % 2 == 0:
                result.append(even_digits[even])
                even+=1
            else:
                result.append(odd_digits[odd])
                odd+=1
        
        final = ''.join(map(str,result))
        return int(final)