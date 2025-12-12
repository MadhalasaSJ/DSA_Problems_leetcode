class Solution:
    def countDigits(self, num: int) -> int:
        val = list(str(num))
        count  = 0
        for ch in val:
            digit = int(ch)
            if num % digit == 0:
                count += 1
        return count        

        