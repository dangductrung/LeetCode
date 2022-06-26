class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        R, C = len(grid), len(grid[0])
        
        seenPoints = []
        maxArea = 0
        def dfs(r, c):
            if not (0 <= r < R and 0 <= c < C and [r,c] not in seenPoints and grid[r][c]):
                return 0
            seenPoints.append([r,c])
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1)
                
        for r in range(R):
            for c in range(C):
                if(grid[r][c] == 1):
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea