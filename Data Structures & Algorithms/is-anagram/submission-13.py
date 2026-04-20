class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict, tDict = {},{}

        for sChar, tChar in zip(s,t):
            sDict[sChar] = 1+sDict.get(sChar, 0)
            tDict[tChar] = 1+tDict.get(tChar, 0)
        
        if sDict == tDict:
            return True
        else:
            return False
        
        