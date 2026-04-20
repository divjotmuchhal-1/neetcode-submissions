class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        res = 0

        for n in nums:
            if (n-1) not in mySet:
                length = 1
                while (n+length) in mySet:
                    length+=1
                res = max(length,res)
        

        return res
            

