class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        limit = len(nums) // 3

        print(limit)

        myDict= {}

        for n in nums:
            myDict[n] = 1 + myDict.get(n,0)
        for number,count in myDict.items():
            if count > limit:
                res.append(number)
        

        return res


        