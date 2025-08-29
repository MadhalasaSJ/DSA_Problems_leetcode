class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      mappin = {}

      for i, n in enumerate(nums):
        diff = target  - n
        if diff in mappin:
            return [mappin[diff], i]
        mappin[n] = i
      return []    
             
           
                                 
        