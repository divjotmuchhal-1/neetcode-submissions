class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            if self.countDict(s2[i:i+len(s1)]) == self.countDict(s1):
                return True
        return False
    
    def countDict(self, string):
        myDict = {}
        for c in string:
            myDict[c] = 1 + myDict.get(c, 0)
        return myDict
        