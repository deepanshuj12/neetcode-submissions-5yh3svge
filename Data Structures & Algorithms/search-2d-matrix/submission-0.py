class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        beg=0
        mid=0
        end=len(matrix[0])-1
        for i in range(len(matrix)):
            if target>matrix[i][-1]:
                continue
            elif target==matrix[i][-1]:
                return True
            for j in range(mid,end):
                mid=(beg+end)//2
                if target>matrix[i][mid]:
                    beg=mid
                elif target<matrix[i][mid]:
                    end=mid
                else:
                    return True
        return False