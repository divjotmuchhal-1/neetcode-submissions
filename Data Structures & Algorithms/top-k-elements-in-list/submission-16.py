from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}

        for n in nums:
            countDict[n] = 1+countDict.get(n,0)

        occurArr = [[] for _ in range(len(nums) + 1) ]

        for n,c in countDict.items():
            occurArr[c].append(n)
        

        res = []
        for i in range(len(occurArr)-1,-1,-1):
            for n in occurArr[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(n)
        
        return res
            

        


        
            