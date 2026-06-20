class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        tCount = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c,0)
        l,r = 0,0
        have,need = 0, len(tCount)
        haveLen = float("inf")
        res = [-1,-1]
        while r < len(s):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in tCount and window[s[r]] == tCount[s[r]]:
                have +=1
            while have == need:
                if (r-l+1) < haveLen:
                    haveLen = (r-l+1)
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in tCount and window[s[l]] < tCount[s[l]]:
                    have-=1
                l+=1
            r+=1
        l,r = res
        if haveLen == float("inf"):
            return ""
        else:
            return s[l:r+1]
                

        