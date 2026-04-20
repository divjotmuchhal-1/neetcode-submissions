class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowLen = len(s1)

        for i in range(len(s2)-windowLen+1):
            if sorted(s1) == sorted(s2[i:i+windowLen]):
                return True
        


        return False
        

        