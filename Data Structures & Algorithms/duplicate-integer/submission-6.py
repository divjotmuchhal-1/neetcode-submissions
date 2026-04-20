class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = []

        for n in nums:
            if n in mySet:
                return True
            else:
                mySet.append(n)
        

        return False
