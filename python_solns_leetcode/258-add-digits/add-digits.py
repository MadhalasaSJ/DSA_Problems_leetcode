class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digit = list(str(num))
            num = sum(int(d) for d in digit)
        return num
        