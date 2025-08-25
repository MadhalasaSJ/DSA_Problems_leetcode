class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapin = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapin:
                return [mapin[diff], i]
            mapin[n] = i
        return []
             
           
                                 
        