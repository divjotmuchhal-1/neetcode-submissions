class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', '}':'{', ']':'['}

        for n in s:
            if  n in closeToOpen:
                if  stack and stack[-1] == closeToOpen[n]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        if not stack:
            return True
        else:
            return False