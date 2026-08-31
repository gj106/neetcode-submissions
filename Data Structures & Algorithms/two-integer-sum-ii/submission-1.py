class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = len(numbers)
        j = l - 1
        i = 0
        sum_val = 0
        while i < j:
            sum_val = numbers[i] + numbers[j]
            if sum_val == target:
                return [i+1, j+1]
            if sum_val < target:
                i=i+1
            else:
                j=j-1
