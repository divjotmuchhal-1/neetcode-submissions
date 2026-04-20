class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for n in nums:
            freqDict[n] = 1 + freqDict.get(n,0)
        

        freq = [[] for _ in range(len(nums)+1)]

        for n,c in freqDict.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                
                res.append(n)
        

        return res
            