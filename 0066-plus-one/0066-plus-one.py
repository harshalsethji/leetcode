class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = []
        string = ''
        for i in digits:
            string += str(i)
        integer = int(string) + 1
        string = str(integer)

        for i in string:
            num.append(int(i))
        return num