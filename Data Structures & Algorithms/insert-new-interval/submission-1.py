class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        sidx = 0
        l = len(intervals)
        res=[]
        while sidx < l: # start of the new interval is always greater than the end of the current interval
            if intervals[sidx][1] < newInterval[0]:
                res.append(intervals[sidx])
                sidx+=1
            else:
                break
        
        while sidx < l: # merge
            if intervals[sidx][0] <= newInterval[1]: # now the end of the cur interval is gereter than the start of the new interval, we check if the start of the cur interval is smaller than the end of the new inderval
                newInterval[0] = min(newInterval[0], intervals[sidx][0])
                newInterval[1] = max(newInterval[1], intervals[sidx][1])
                sidx+=1
            else:
                break
        res.append(newInterval)

        while sidx < l:
            if intervals[sidx][0] > newInterval[1]:  # now the reaining cases where the start of the cur interval is greater than the end of the newInterval
                res.append(intervals[sidx])
                sidx+=1
            else:
                break
        
        return res

            
