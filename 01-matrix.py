"""

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.


Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

Time Complexity: 
- method 1: O(m * n) 
- method 2: O(m * n)

Space Complexity: 
- method 1: O(m * n) - Extra space for matrix copy and seen set.
- method 2: O(m * n) - Queue stores at most all elements in the worst case.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach: 
# use Breadth-First Search (BFS) to find the shortest distance of each cell from the nearest 0. 
# In method 1, we use an explicit set to track visited cells, while in method 2, we modify the input matrix directly. 
# Both methods initialize the queue with all 0s and update neighboring cells in BFS order to ensure minimum distance propagation.

from queue import Queue

class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m = len(mat)
        n = len(mat[0])
        
        # Method 1: BFS with a separate matrix copy
      
        matrix = [row[:] for row in mat]
        q = Queue()
        seen = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.put((i, j, 0))
                    seen.add((i, j))

        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while not q.empty():
            r, c, steps = q.get()

            for dr, dc in direct:
                next_r, next_c = r+dr, c+dc

                if (next_r, next_c) not in seen and 0 <= next_r < m and 0 <= next_c < n:
                    seen.add((next_r, next_c))
                    q.put((next_r, next_c, steps+1))
                    matrix[next_r][next_c] = steps + 1

        return matrix



        # Method 2: BFS modifying input matrix directly
      
        q = Queue()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.put((i, j))
                else:
                    mat[i][j] = float("inf")

        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while not q.empty():
            r, c = q.get()

            for dr, dc in direct:
                next_r, next_c = r+dr, c+dc

                if 0 <= next_r < m and 0 <= next_c < n and mat[next_r][next_c] > mat[r][c] + 1:
                    mat[next_r][next_c] = mat[r][c] + 1
                    q.put((next_r, next_c))

        return mat

       
