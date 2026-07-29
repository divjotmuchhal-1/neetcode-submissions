class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        
        for i,h in enumerate(heights):
            start = i 
            while stack and h < stack[-1][1]:
                stackInd, stackH = stack.pop()
                area = (i-stackInd) * stackH
                maxArea = max(area,maxArea)
                start = stackInd
            stack.append([start, h])
        
        for i,h in stack:
            maxArea = max((len(heights)- i)  * h, maxArea)
        
        return maxArea
        

        