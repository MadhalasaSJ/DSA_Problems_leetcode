class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_index = {}

        for i,n in enumerate(nums):
            diff = target - n 
            if diff in map_index:
                return [map_index[diff], i]
            map_index[n] = i
        return []                 
        