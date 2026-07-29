class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 1
        numSet = set(nums)
        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                    res = max(length, res)
        return res

        