class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tDict, sDict = {}, {}    

        for i in range(len(s)):
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
        if tDict == sDict:
            return True
        else:
            return False    