class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0 
        r = k

        while r < len(nums)+1:
            res.append(max(nums[l:r]))
            r+=1
            l+=1
        
        return res

        