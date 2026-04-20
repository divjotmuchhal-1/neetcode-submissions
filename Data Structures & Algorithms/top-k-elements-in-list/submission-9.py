class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = {}
        for n in nums:
            countNums[n]  = 1+countNums.get(n,0)

        freq = [[] for i in range(len(nums)+1)]

        for n, c in countNums.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        
        return []











        
        