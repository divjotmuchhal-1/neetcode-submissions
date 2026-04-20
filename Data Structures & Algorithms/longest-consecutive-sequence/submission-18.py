class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        for n in nums:
            if(n-1) not in numSet:
                count = 1
                while(n+1) in numSet:
                    count += 1
                    n+=1
                res = max(res,count)
        

        return res
 

