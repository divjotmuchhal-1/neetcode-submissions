class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myDict = {}
        l = 0
        res = 0
        for r in range(len(s)):
            myDict[s[r]] = 1 + myDict.get(s[r], 0)
            if (r-l+1) - max(myDict.values()) > k:
                myDict[s[l]]-=1
                l+=1
            res = max(res, (r-l+1))
        return res

        