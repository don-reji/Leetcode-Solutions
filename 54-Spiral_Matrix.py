# link - https://leetcode.com/problems/spiral-matrix/
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    top = 0
    bottom = len(matrix)
    l = 0
    r = len(matrix[0])
    res = []
    
    while l<r and bottom > top:
        # get all top elements and bring top 1 row down
        for i in range(l,r):
            res.append( matrix[top][i] )
        top += 1
        
        # get all right side elements and move right by 1 column left 
        for i in range( top,bottom ):
            res.append( matrix[i][r-1] )
        r -= 1

        # condition to stop when all elements are in res
        if not (  l<r and top < bottom  ):
            break

        # get all bottom elements and move bottom 1 row above
        for i  in range(  r-1 , l-1 , -1  ):
            res.append( matrix[bottom-1][i] )
        bottom-=1

        # get all left element and move left column by 1 row to right
        for i in range( bottom-1, top-1, -1  ):
            res.append( matrix[i][0] )
        l+=1

    return res

    # O(m*n) space and time