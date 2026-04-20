class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")": "(", "}": "{", "]":"["}
        stack = []

        for c in s:
            if c in closeToOpen.keys() and stack:
                if stack[-1] != closeToOpen[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        

        
        if len(stack) == 0:
            return True
        else:
            return False
        