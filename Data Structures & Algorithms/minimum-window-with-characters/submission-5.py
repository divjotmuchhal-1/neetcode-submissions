class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        #edge cases
        if(len(t) > len(s) or t == ""):
            return ""

        countS, countT = {}, {}
        # creating dictionary for number of occurances of each characters
        # in the substring
        for c in t:
            countT[c] = 1+countT.get(c,0)

        
        resLen, res = float("infinity"), [-1,-1]
        have, need = 0, len(countT)

    
        l = 0
        for r in range(len(s)):
            #creating dictionary for number of occurances od characters
            #in s string 
            c = s[r]
            countS[c] = 1+countS.get(c, 0)
            #checking if we have the right number of occurances of a certain character
            if c in countT and countS[c] == countT[c]:
                have+=1
            # shifting left to try to optimize substring
            while have == need:
                if (r-l+1) < resLen:
                    resLen = (r-l+1)
                    res = [l, r]
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l, r = res
        if(resLen == float("infinity")):
            return ""
        else:
            return s[l:r+1]
                

                


        
        


