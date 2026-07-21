class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        res = []
        currStr = []
        def dfs(i):
            if i == len(digits):
                res.append("".join(currStr))
                return
            
            for c in digitToChar[int(digits[i])]:
                currStr.append(c)
                dfs(i+1)
                currStr.pop()
            
        if digits:
            dfs(0)
        return res
        