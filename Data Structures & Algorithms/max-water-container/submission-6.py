class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxx = 0

        while l <r:
            area = (r-l) * min(heights[l],heights[r])
            maxx = max(area,maxx)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        
        return maxx

