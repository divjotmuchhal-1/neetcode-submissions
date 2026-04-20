class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0, len(s)-1
        while l < r:
            while l<r and  self.helper(s[l]) == False:
                l+=1
            while l< r and self.helper(s[r]) == False:
                r-=1
            if l < r and s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True

    def helper(self,c):
        if ord('0') <= ord(c) <= ord('9'):
            return True
        elif ord('a') <= ord(c) <= ord('z'):
            return True
        else:
            return False
        
        