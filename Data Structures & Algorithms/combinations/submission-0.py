class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(num, i):
            if i == k:
                res.append(subset.copy())
                return
            if num > n:
                return

            subset.append(num)
            dfs(num+1, i+1)
            subset.pop()
            dfs(num+1, i)
        dfs(1, 0)
        return res