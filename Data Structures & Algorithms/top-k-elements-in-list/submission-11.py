from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mySet = {}

        for n in nums:
            mySet[n] = 1 + mySet.get(n, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in mySet.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []
