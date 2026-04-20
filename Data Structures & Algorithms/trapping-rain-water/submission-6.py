class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lMax, rMax = height[l], height[r] 
        res = 0

        while l <= r:
            if lMax < rMax:
                lMax = max(height[l], lMax)
                res += (lMax - height[l])
                l+=1
            else:
                rMax = max(height[r], rMax)
                res += rMax-height[r]
                r-=1
        

        return res

        