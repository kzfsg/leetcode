class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] # down, right, up, left

        def dfs(grid, curr):
            if (0 > curr[0] or curr[0] >= len(grid)
            or 0 > curr[1] or curr[1] >= len(grid[0])
            or grid[curr[0]][curr[1]] == '0' ): # check if node has been visited or oob
                return

            else:
                grid[curr[0]][curr[1]] = '0' # mark as visited
                
                for coords in directions: # recurse in all directions
                    dfs(grid, [coords[0] + curr[0], coords[1] + curr[1]])

        islandCounter = 0
        for row in range(len(grid)): 
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(grid, [row, col])
                    islandCounter += 1

        return islandCounter
            

        

# directions
# if curr node is unvisited, run dfs, travels in all directions and marks nodes as visited
# for every count of dfs, incr island counter by 1
# if all nodes are visited, return island count