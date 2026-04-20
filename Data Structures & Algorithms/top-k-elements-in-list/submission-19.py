class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        charOccurances = {}
        for n in nums:
            charOccurances[n] = 1 + charOccurances.get(n,0)
        
        occurancesArray = [[] for _ in range(len(nums)+1)]

        for n,c in charOccurances.items():
            occurancesArray[c].append(n)
        
        res = []
        for i in range(len(occurancesArray)-1,-1,-1):
            for n in occurancesArray[i]:
                if len(res) == k:
                    return res
                else:
                    res.append(n)
        
        return res
                

        



        
        