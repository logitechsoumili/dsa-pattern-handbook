class Solution:
    def isIntersect(self, intervals):
        intervals.sort()
        
        start1, end1 = intervals[0]
        
        flag = False
        
        for i in range(1, len(intervals)):
            start2, end2 = intervals[i]
            
            if end1 >= start2:
                flag = True
                break
            
            start1, end1 = start2, end2
                
        return flag