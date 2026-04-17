class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap={}
        for row in range(9):
            hmap.clear()
            for col in range(9):
                if board[row][col]==".":
                    continue
                elif board[row][col] not in hmap:
                    hmap[board[row][col]]=hmap.get(board[row][col],0)+1
                else:
                    return False
        for col in range(9):
            hmap.clear()
            for row in range(9):
                if board[row][col]==".":
                    continue
                elif board[row][col] not in hmap:
                    hmap[board[row][col]]=hmap.get(board[row][col],0)+1
                else:
                    return False
        for i in range(3):
            for j in range(3):
                hmap.clear()
                for row in range(3*i,3*i+3,1):
                    for col in range(3*j,3*j+3,1):
                        if board[row][col]==".":
                            continue
                        elif board[row][col] not in hmap:
                            hmap[board[row][col]]=hmap.get(board[row][col],0)+1
                        else:
                            return False
        return True









