class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = {}
        for n in nums:
            myDict[n] = 1 + myDict.get(n,0)
        freq_arr = [[] for _ in range(len(nums)+1)]
        for n,c in myDict.items():
            freq_arr[c].append(n)
        res = []
        for i in range(len(freq_arr)-1,-1,-1):
            for n in freq_arr[i]:
                if len(res) == k:
                    return res
                res.append(n)
        
        return res


        