class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tDict, sDict = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            tDict[t[i]] = 1 + tDict.get(t[i], 0)
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
        return (tDict == sDict)

        