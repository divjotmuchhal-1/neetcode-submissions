class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        charDict = {}

        for r in range(len(s)):
            charDict[s[r]] = 1+charDict.get(s[r],0)
            while ((r-l+1) - (max(charDict.values()))) > k:
                charDict[s[l]] -= 1
                l+=1
            res = max(res,(r-l+1))
        

        return res