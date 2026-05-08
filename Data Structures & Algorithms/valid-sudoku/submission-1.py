class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rHashset = set()
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in rHashset:
                    return False
                else:
                    rHashset.add(board[i][j])
                
        for j in range(len(board[0])):
            cHashset = set()
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in cHashset:
                    return False
                else:
                    cHashset.add(board[i][j])
        gHashset = set()
        for box_row in [0,3,6]:
            for box_col in [0,3,6]:
                for i in range(3):
                    for j in range(3):
                        cell = board[box_row+i][box_col+j]
                        if cell == ".":
                            continue
                        elif cell in gHashset:
                            return False
                        else:
                            gHashset.add(cell)
                gHashset.clear()
        return True