class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for n in nums:
            myDict[n] = 1 + myDict.get(n,0)
        occurances = [[] for _ in range(len(nums)+1)]
        for n,c in myDict.items():
            occurances[c].append(n)
        res = []
        for i in range(len(occurances)-1,-1,-1):
            for n in occurances[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(n)
        
        return res
        