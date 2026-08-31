class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        myDict = {}
        res = []
        for name,height in zip(names,heights):
            myDict[height] = name
        
        heights.sort(reverse = True)
        for height in heights:
            res.append(myDict[height])
        return res

        