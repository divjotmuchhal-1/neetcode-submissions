class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                box = board[i][j]

                if box == ".":
                    continue
                if box in rows[i]:
                    return False
                if box in cols[j]:
                    return False
                if box in boxes[(i//3, j//3)]:
                    return False
                
                rows[i].add(box)
                cols[j].add(box)
                boxes[(i//3,j//3)].add(box)
        return True
                
        