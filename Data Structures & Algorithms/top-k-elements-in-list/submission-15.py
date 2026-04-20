class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        freqArray = [[] for _ in range(len(nums) +1 )]
        res  = []

        for n in nums:
            freqDict[n] = 1+ freqDict.get(n,0)
        
        for n,c in freqDict.items():
            freqArray[c].append(n)
        

        for i in range(len(freqArray)-1,-1,-1):
            for n in freqArray[i]:
                res.append(n)
                if len(res) >= k:
                    return res

        

        return res
    


        

