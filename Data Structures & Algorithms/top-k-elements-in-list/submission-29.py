class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        freq = [[] for _ in range(len(nums)+1)]
        for n,c in counts.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                if len(res) == k:
                    return res
                res.append(n)
        return res
        