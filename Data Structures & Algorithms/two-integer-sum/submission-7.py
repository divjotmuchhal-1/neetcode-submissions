class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i,num in enumerate(nums):
            if target - num in myDict.keys():
                return [myDict.get(target-num),i]
            else:
                myDict[num] = i
        return []




            
        
        