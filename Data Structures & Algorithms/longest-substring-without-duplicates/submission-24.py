class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in mySet:
                mySet.remove(s[l])
                l+=1
            res = max(res, (r-l+1))
            mySet.add(s[r])
        return res

        