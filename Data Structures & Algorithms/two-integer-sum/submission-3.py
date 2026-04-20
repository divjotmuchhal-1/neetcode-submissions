class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i,num in enumerate(nums):
            val = target - num
            if val in myDict:
                return [myDict[val],i]
            else:
                myDict[num] = i
        return
            