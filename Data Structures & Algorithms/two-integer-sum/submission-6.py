class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mySet = {}

        for i, a in enumerate(nums):
            res = target - a
            if res in mySet:
                return [mySet[res], i]
            else:
                mySet[a] = i
        return []


            
        
        