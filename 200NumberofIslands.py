class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0 
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]] # right, left, up, down

        def dfs(r,c):
            visited.add((r,c))
            for first, second in directions:
                if 0 <= r + first < rows and 0 <= c + second < cols and (r + first, c + second) not in visited and grid[r + first][c + second] == "1":
                    dfs(r + first, c + second)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands += 1
        return islands
