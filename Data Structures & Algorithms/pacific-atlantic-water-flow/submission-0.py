class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac_reach = set()
        atl_reach = set()
        n = len(heights)
        m = len(heights[0])


        def dfs(r,c,reach_set,height):

            if (r < 0 or c < 0) \
            or (r >= n or c >= m) \
            or ((r,c) in reach_set) \
            or (heights[r][c] < height): # water cant flow to a height which is bigger
                return
            
            reach_set.add((r,c))

            dfs(r-1, c, reach_set, heights[r][c])
            dfs(r+1, c, reach_set, heights[r][c])
            dfs(r, c-1, reach_set, heights[r][c])
            dfs(r, c+1, reach_set, heights[r][c])

            return

        for i in range(n):
            dfs(i,0,pac_reach,heights[i][0])
            dfs(i,m-1,atl_reach,heights[i][m-1])
        
        for j in range(m):
            dfs(0,j,pac_reach,heights[0][j])
            dfs(n-1,j,atl_reach,heights[n-1][j])

        res = []
        for r in range(n):
            for c in range(m):
                if (r,c) in pac_reach and (r,c) in atl_reach:
                    res.append([r,c])           

        return res

