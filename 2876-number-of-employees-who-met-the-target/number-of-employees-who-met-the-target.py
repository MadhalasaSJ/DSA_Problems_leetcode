class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        #Method 1
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count 
        
        