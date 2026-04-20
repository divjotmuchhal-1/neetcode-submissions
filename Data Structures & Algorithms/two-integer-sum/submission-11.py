class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i, n in enumerate(nums):
            if (target - n) in  myDict:
                return [myDict[target-n], i]
            else:
                myDict[n] = i
        

