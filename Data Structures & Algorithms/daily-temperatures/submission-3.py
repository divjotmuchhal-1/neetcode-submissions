class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                Temp, Ind = stack.pop()
                res[Ind] = i-Ind
            
            stack.append([n,i])
        

        return res