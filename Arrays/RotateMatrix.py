from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in matrix:
            print(row)
        
        m=len(matrix)
        n=len(matrix[0])
        print(f"size={m}x{n}")
        #print(*matrix)
        t = [[matrix[j][i] for j in range(m)] for i in range(n)]
        for row in t:
            print(row)
        print("------------------")
        l,r=0,n-1
        while(l < r):
            for row in range(m):
                print(f"{matrix[row][l]}", end=" ")
                t[row][l],t[row][r] = t[row][r], t[row][l]
            l += 1
            r -= 1

        print("------------------")
        for row in t:
            print(row)



matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)