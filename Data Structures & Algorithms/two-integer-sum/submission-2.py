class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i,j in enumerate(nums):
            val = target-j
            if val in myDict:
                return [myDict[val], i]
            else:
                myDict[j] = i
        return
        