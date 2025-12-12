class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        #Method 1
        #count = 0
        #for i in hours:
            #if i >= target:
                #count += 1
        #return count 
        #Method 2   
        return sum(1 for h in hours if h >= target)
        