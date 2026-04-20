class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set()
        for num in nums: 
            mySet.add(num)
        return len(mySet) != len(nums)

         