class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals is None:
            return None
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
 
        # [[1,3],[1,5]]
        # [[1,3]]
        for idx in range(1, len(intervals)):
            if intervals[idx][0] <= res[-1][1]:
                res[-1][1] = max(intervals[idx][1], res[-1][1])
            else:
                res.append(intervals[idx])
        
        return res