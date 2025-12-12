class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sums = 0
        d_sum = 0
        for a in nums:
            sums += a

        for b in nums:
            for digit in str(b):
                d_sum += int(digit)

        return abs(sums-d_sum)        


        