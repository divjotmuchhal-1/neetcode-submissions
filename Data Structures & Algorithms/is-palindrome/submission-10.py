class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newString = ""

        for c in s:
            if self.isalnum(c):
                newString +=c
        

        l,r = 0, len(newString)-1
        while l < r:
            if newString[l] != newString[r]:
                return False
            else:
                l+=1
                r-=1
        

        return True




    def isalnum(self, c):
        if ord('a') <= ord(c) <= ord('z'):
            return True
        

        elif ord('0') <= ord(c) <= ord('9'):
            return True
        else:
            return False
        