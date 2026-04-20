class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for n in nums:
            currSequence = 0
            if (n-1) not  in mySet:
                while n in mySet:
                    currSequence += 1
                    n+=1
            longest = max(longest, currSequence)
        return longest
            
        


