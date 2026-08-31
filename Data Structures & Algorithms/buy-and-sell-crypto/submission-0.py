class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if prices is None:
            return 0 
        global_min = prices[0]
        res = 0
        for pr in prices:
            global_min = min(global_min, pr)
            res = max(res, pr - global_min )

        return res