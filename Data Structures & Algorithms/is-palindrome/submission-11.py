class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l,r = 0, len(s)-1

        while l <= r:
            while l < r and not self.isalnu(s[l]):
                l+=1
            while l <r and not self.isalnu(s[r]):
                r-=1
            
            if s[r] == s[l]:
                r-=1
                l+=1
            else:
                return False
        

        return True
    



    def isalnu(self,c):
        if ord('a') <= ord(c) <= ord('z'):
            return True
        
        if ord('0') <= ord(c) <= ord('9'):
            return True
        
        return False