class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for n in nums:
            mySet.add(n)
        
        if len(mySet) != len(nums):
            return True
        else:
            return False