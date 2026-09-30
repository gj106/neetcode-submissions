class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        n = len(grid)
        m = len(grid[0])

        def dfs(r,c,visted):

            if r < 0 or r >= n \
            or c < 0 or c >=m \
            or (r,c) in visited \
            or grid[r][c] == "0":
                return

            if grid[r][c] == "1":
                visited.add((r,c))

            dfs(r-1, c, visited)
            dfs(r+1, c, visited) 
            dfs(r, c-1, visited)
            dfs(r, c+1, visited)

            return 

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(i,j,visited)
                    res+=1 

        return res       