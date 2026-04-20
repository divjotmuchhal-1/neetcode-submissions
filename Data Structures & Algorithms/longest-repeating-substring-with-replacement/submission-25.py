class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        myDict = {}
        res = 0
        maxfreq = 0
        for r in range(len(s)):

            myDict[s[r]] = 1+myDict.get(s[r], 0)
            maxfreq = max(maxfreq, myDict[s[r]])
            if (r-l+1) - maxfreq > k:
                myDict[s[l]] -= 1
                l+=1
            
            res = max(res, (r-l+1))
        
        return res