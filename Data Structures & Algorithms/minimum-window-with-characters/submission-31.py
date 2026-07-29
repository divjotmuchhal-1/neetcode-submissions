class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t) #Dictionary [t[i], count]
        myDict = {}
        res, resLen = [-1,-1], float('inf')
        have, need = 0, len(tCount)
        l = 0
        for r in range(len(s)):
            myDict[s[r]] = 1 + myDict.get(s[r],0)
            if s[r] in tCount and myDict[s[r]] == tCount[s[r]]:
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    resLen = (r-l+1)
                    res = [l,r]
                myDict[s[l]] -= 1
                if s[l] in tCount and myDict[s[l]] < tCount[s[l]]:
                    have-=1
                l+=1
            
        l,r = res
        if resLen == float('inf'):
            return ""
        else:
            return s[l:r+1]


        

        