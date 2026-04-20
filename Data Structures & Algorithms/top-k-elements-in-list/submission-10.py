class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mySet = {}

        for n in nums:
            mySet[n] = 1+mySet.get(n,0)
        
        arr = [[] for i in range(len(nums)+1)]

        for n,c in mySet.items():
            arr[c].append(n)
        
        res = []
        count = 0
        for i in range(len(arr)-1,-1,-1):
            for num in arr[i]:
                res.append(num)
                count+=1
            if count == k:
                return res
        return []
        

        