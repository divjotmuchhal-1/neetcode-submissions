class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                area = height * (i-index)
                start = index
                maxArea = max(maxArea,area)
            stack.append((start,h))
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
        return maxArea
        
        