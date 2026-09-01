class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sumarray = -100001
        maxsumarray = -100001

        for num in nums:
            # if nums[j] > sumarray + nums[j]:
            #     sumarray = nums[j]
            # else:
            #     sumarray = sumarray + nums[j]
            sumarray = max(num, sumarray + num)

            maxsumarray = max(sumarray, maxsumarray)
        return maxsumarray

        