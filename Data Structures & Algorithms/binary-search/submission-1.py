class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            number = nums[(l+r)//2]

            if number < target:
                l+=1
            elif number > target:
                r-=1
            else:
                return (l+r)//2
        
        return -1

        