from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)
        
        occur = [[] for _ in range(len(nums)+1)]

        for n,c in count.items():
            occur[c].append(n)
        
        res = []
        for i in range(len(occur)-1,-1,-1):
            for n in occur[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(n)
        
        return res
   