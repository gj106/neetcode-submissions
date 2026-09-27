class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        i = 0
        j = 1
        res = 0
        n = len(intervals)

        if n == 0:
            return 0
        
        intervals.sort(key=lambda x: x[0])

        while i < n and j < n: 
            if intervals[i][1]>intervals[j][0]:
                res += 1
                intervals[i][1] = min(intervals[i][1],intervals[j][1] )
            else:
                i = j
            j+=1
        
        return res
