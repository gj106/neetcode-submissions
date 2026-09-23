class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights) - 1
        mleft = mright = mArea = float("-inf")

        while i < j:

            mArea = max(min(heights[i],heights[j])*(j-i), mArea)

            if heights[i] < heights[j]:
                i +=1
            else:
                j-=1

        return mArea