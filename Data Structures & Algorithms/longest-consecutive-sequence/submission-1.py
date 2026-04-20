class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        mySet = set(nums)
        mySet = sorted(mySet)
        myList = list(mySet)

        sizes = []
        size = 1
        for i, num in enumerate(myList):
            if i < len(myList)-1 and myList[i] == myList[i+1]-1:
                size += 1
            else:
                sizes.append(size)
                size = 1
        return max(sizes)





        