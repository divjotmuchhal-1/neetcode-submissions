class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for n in nums:
            myDict[n] = 1 + myDict.get(n,0)
        occurancesArray = [[] for _ in range(len(nums)+1)]
        
        for n,c in myDict.items():
            occurancesArray[c].append(n)
        res = []
        for i in range(len(occurancesArray)-1,-1,-1):
            for n in occurancesArray[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(n)
        

        return res

        
        