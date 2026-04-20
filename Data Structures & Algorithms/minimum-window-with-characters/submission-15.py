class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        tDict, window = {}, {}
        l= 0
        res, resLen = [-1,-1], float("infinity")
        for c in t:
            tDict[c] = 1 + tDict.get(c, 0)

        have, need = 0, len(tDict)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0 )

            if s[r] in tDict and window[s[r]] == tDict[s[r]]:
                have+=1

            while have == need:

                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                
                window[s[l]] -=1
                if s[l] in tDict and window[s[l]] < tDict[s[l]]:
                    have -= 1
                l+=1
        l,r = res

        if resLen == float("infinity"):
            return ""
        else:
            return s[l:r+1]





        
        