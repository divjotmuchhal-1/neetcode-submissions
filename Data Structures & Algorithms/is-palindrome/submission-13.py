class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0, len(s)-1

        while l <= r:
            while l < r and  not self.isalphanumerical(s[l]):
                l+=1
            while  l< r and  not self.isalphanumerical(s[r]):
                r-=1
            
            if s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True

    def isalphanumerical(self,c):
        if ord('a') <= ord(c) <= ord('z'):
            return True
        
        elif ord('0') <= ord(c) <= ord('9'):
            return True
        
        elif ord("A") <= ord(c) <= ord("Z"):
            return True
        else:
            return False