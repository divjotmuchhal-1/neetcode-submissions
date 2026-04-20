class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        res = 0

        for i in range(len(nums)):
            if nums[i]-1 not in mySet:
                length = 1
                while nums[i]+length in mySet:
                    length+=1
                res = max(length,res)
        

        return res

