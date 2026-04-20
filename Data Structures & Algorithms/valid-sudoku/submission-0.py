
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking rows
        mySet = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num != '.':
                    if num in mySet:
                        return False
                    else:
                        mySet.add(num)
            mySet.clear()

        # Checking columns
        mySet = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[j][i]
                if num != '.':
                    if num in mySet:
                        return False
                    else:
                        mySet.add(num)
            mySet.clear()

        # Checking 3x3 squares
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                mySet = set()
                for k in range(3):
                    for l in range(3):
                        num = board[i + k][j + l]
                        if num != '.':
                            if num in mySet:
                                return False
                            else:
                                mySet.add(num)
        
        return True
