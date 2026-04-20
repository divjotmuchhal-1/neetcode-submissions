class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, tDict = {}, {}
        for c in t:
            tDict[c] = 1 + tDict.get(c,0)
        res, resLen = [-1,-1], float('inf')
        have, need = 0, len(tDict)
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in tDict and window[c] == tDict[c]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                window[s[l]]-=1
                if s[l] in tDict and window[s[l]] < tDict[s[l]]:
                    have-=1
                l+=1
        l,r = res
        if resLen == float('inf'):
            return ""
        else:
            return s[l:r+1]

        
        