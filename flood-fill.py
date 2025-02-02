"""

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.

Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]


Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

Time Complexity: O(N*M) in the worst case, where N is the number of rows and M is the number of columns, since we may visit every pixel once.
Space Complexity: O(N*M) in the worst case due to the recursive call stack in DFS if all pixels need to be changed.

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Approach:
# 1. Use Depth-First Search (DFS) to traverse the image starting from (sr, sc) and change all connected pixels with the same old_color to the new color.
# 2. Recursively explore four possible directions (up, left, down, right) while ensuring boundary conditions are met.
# 3. If the starting pixel already has the target color, return the image without making changes to avoid unnecessary recursion.


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(image, sr, sc, old_color, new_color):

            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != old_color:
                return

            image[sr][sc] = new_color
            direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

            for dr, dc in direct:
                dfs(image, sr+dr, sc+dc, old_color, new_color)


        old_color = image[sr][sc]
        if old_color != color:
            dfs(image, sr, sc, old_color, color)

        return image
