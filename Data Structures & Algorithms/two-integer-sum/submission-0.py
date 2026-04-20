class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in myDict:
                return myDict[diff],i
            myDict[n] = i



        