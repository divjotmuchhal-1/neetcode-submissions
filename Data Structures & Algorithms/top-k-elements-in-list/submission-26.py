class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        for n in nums:
            numCount[n] = 1 + numCount.get(n,0)
        freqArr = [[] for _ in range(len(nums)+1)]
        for n,c in numCount.items():
            freqArr[c].append(n)
        res = []
        for i in range(len(freqArr)-1,-1,-1):
            for n in freqArr[i]:
                if len(res) == k:
                    return res
                res.append(n)
        return res


        