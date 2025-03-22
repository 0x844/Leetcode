class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = {}
        count = 0
        col = len(grid[0])
        for row in grid:
            if tuple(row) in hashmap:
                hashmap[tuple(row)] += 1
            else:
                hashmap[tuple(row)] = 1 # tuple since you can't use list as dict key
        for i in range(len(grid)):
            lst = [] # store col here
            for j in range(col):
                lst.append(grid[j][i])
            if tuple(lst) in hashmap:
                count += hashmap[tuple(lst)]
        return count
