from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        for n in nums:
            myDict[n] = 1+myDict.get(n,0)
        
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for n,c in myDict.items():
            freq[c].append(n)

        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(num)
        return res
