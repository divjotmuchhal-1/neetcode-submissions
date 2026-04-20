class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        res = 0

        while l < r:
            if lmax < rmax:
                l+=1
                lmax = max(height[l], lmax)
                res += lmax - height[l]
            else:
                r-=1
                rmax= max(height[r], rmax)
                res += rmax - height[r]
        
        return res
        




[0,2,0,3,1,0,1,3,2,1]

lMax = 0
rMax = 1



        