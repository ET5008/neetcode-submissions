from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 0
        tileQueue = deque([])
        seen = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in seen:
                    seen.add((r, c))
                    tempQueue = deque([(r, c)])
                    island += 1
                    while (len(tempQueue) != 0):
                        cr, cc = tempQueue.popleft()

                        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
                        for nr, nc in directions:
                            row = cr + nr
                            col = cc + nc
                            if (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"):
                                if ((row, col) not in seen):
                                    seen.add((row, col))
                                    tempQueue.append((row, col))
        return island
                

            
        