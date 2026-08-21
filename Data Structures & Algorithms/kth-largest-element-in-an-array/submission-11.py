import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def quickselect(l,r):
            rand = random.randint(l,r)
            nums[r], nums[rand] = nums[rand], nums[r]
            pivot, p = nums[r], l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            elif p > k:
                return quickselect(l,p-1)
            else:
                return quickselect(p+1,r)
        return quickselect(0, len(nums)-1)





        