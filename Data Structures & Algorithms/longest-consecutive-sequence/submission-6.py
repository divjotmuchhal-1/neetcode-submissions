class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0

        for n in mySet:
            # check if its the start of a sequence
            if (n-1) not in mySet:
                length = 0
                while(n + length) in mySet:
                    length += 1
                longest = max(longest,length)
        return longest





        