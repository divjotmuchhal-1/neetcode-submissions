class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                square = board[i][j]
                if square in rows[i]:
                    return False
                if square in cols[j]:
                    return False
                if square in boxes[(i//3,j//3)]:
                    return False
                
                rows[i].add(square)
                cols[j].add(square)
                boxes[(i//3,j//3)].add(square)
        return True
        