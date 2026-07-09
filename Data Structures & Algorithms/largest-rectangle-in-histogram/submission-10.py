class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i,h in enumerate(heights):
            start = i
            while stack and  h < stack[-1][1]:
                index,height = stack.pop()
                area = height * (i-index)
                maxArea = max(maxArea,area)
                start = index
            stack.append([start,h])
        
        for i,h in stack:
            maxArea = max(maxArea, (len(heights)-i) * h )
        
        return maxArea

