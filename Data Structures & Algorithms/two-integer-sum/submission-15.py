class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numArr = {}
        for i,n in enumerate(nums):
            if (target - n) in numArr:
                return [numArr[(target-n)], i]
            numArr[n] = i
        

