class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        myDict = defaultdict(int)
        res = 0
        for r in range(len(s)):
            myDict[s[r]] +=1
            while (r-l+1) - max(myDict.values()) > k:
                myDict[s[l]]-=1
                l+=1
            res = max(res, (r-l+1))
        
        return res
        