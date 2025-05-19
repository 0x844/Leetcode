class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        visited = set()

        def dfs(r,c,area):
            visited.add((r,c))
            for le, ri in directions:
                if 0 <= le + r < rows and 0 <= ri + c < cols and (le + r,ri + c) not in visited and grid[le+r][ri+c] == 1:
                    area += dfs(le + r, ri + c, 1) # increment area by 1 every time we encounter a "1" block (area is total # of "1" blocks)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_area = max(max_area, dfs(r,c,1))
        return max_area
