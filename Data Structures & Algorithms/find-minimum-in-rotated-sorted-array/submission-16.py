class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0,len(nums)-1

        while l <= r:
            mid = (l+r)//2
            res = min(nums[mid],res)
            if nums[l] < nums[r]:
                return min(nums[l],res)
            

            if nums[l] <= nums[mid]:
                l = mid+1
            if nums[mid] < nums[r]:
                r = mid-1
        return res
            

            
                