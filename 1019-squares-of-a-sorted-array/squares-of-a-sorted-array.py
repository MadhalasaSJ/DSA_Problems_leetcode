class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        nums.sort()
        res = []
        square = 0
        for i in range(len(nums)):
            square = nums[i] * nums[i]
            res.append(square)
            res.sort()
        return res    
        