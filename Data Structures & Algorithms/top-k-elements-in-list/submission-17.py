from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        charCount = {}

        for n in nums:
            charCount[n] = 1+charCount.get(n,0)
        arr = [[] for _ in range(len(nums)+1) ]
        for n,c in charCount.items():
            arr[c].append(n)
        

        res = []
        for i in range(len(arr)-1,-1,-1):
            for n in arr[i]:
                if len(res) == k:
                    return res
                res.append(n)
        

        return res
        