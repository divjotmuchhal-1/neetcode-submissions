from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}

        for n in nums:
            myDict[n] = 1+myDict.get(n,0)
        
        freq = [[] for i in range(len(nums)+1)]

        for key,value in myDict.items():
            freq[value].append(key)
        

        res = []
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(num)
        
        return res
            






