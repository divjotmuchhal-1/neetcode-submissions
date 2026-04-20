class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        s = s.lower()

        while l <= r:
            while l <r and not self.ischarNum(s[l]):
                l+=1
            while l < r and not self.ischarNum(s[r]):
                r-=1
            if l <= r and l >= 0 and s[l] == s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
            
    


    
    
    
    def ischarNum(self,c):
        if ord("0") <= ord(c) <= ord("9"):
            return True
        elif ord("a") <= ord(c) <= ord("z"):
            return True
        elif ord("A") <= ord(c) <= ord("Z"):
            return True
        else:
            return False
