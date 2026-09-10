class Solution:
    def trap(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1
        water = 0
        maxl = 0
        maxr = 0
        while i < j:
            if height[i] < height[j]:
                maxl = max(maxl, height[i])
                water += maxl - height[i]
                i+=1
            else:
                maxr = max(maxr, height[j])
                water += maxr - height[j]
                j-=1
        return water
        