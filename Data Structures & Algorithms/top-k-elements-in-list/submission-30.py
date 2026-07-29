class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        occ = [[] for _ in range(len(nums)+1)]
        for n,c in counts.items():
            occ[c].append(n)
        res = []
        for i in range(len(occ)-1,-1,-1):
            for n in occ[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(n)
        return res


        