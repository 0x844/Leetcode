class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mins = 0
        fresh_oranges = 0 
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c)) # add all rotting oranges to queue 
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # run bfs til fresh_oranges is > 0
        while queue and fresh_oranges > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for le, ri in directions:
                    if 0 <= le + r < rows and 0 <= ri + c < cols and grid[le+r][ri+c] == 1:
                        grid[le+r][ri+c] = 2
                        fresh_oranges -= 1
                        queue.append((le+r, ri+c))
            mins += 1
        if fresh_oranges == 0:
            return mins
        return -1
