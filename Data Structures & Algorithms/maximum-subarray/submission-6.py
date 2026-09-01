class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i, j = 0, 0
        sumarray = -100001
        maxsumarray = -100001

        while j < len(nums):
            # if nums[j] > sumarray + nums[j]:
            #     sumarray = nums[j]
            # else:
            #     sumarray = sumarray + nums[j]
            sumarray = max(nums[j], sumarray + nums[j])

            maxsumarray = max(sumarray, maxsumarray)
            j += 1
        return maxsumarray

        