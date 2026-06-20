class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myDict = {}
        l,r = 0,0
        res = 0
        while r < len(s):
            myDict[s[r]] = 1+ myDict.get(s[r],0)
            while (r-l+1) - max(myDict.values()) > k:
                myDict[s[l]]-=1
                l+=1
            else:
                res = max(r-l+1,res)
            r+=1
        return res
            


        