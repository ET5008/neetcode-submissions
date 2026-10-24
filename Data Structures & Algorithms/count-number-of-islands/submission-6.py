from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        IslandCount = 0
        IslandTileQueue = deque([])
        usedTiles = set()

        for rowIndex in range(len(grid)):
            for colIndex in range(len(grid[0])):
                if grid[rowIndex][colIndex] == "1":
                    IslandTileQueue.append((rowIndex, colIndex))
        
        while (len(IslandTileQueue) > 0):
            initialTile = IslandTileQueue.pop()
            tempQueue = deque([])
            tempQueue.append(initialTile)
            prevUsedLen = len(usedTiles)
            while (len(tempQueue) > 0):
                currentTile = tempQueue.pop()
                if currentTile not in usedTiles:
                    usedTiles.add(currentTile)
                    rowIndex = currentTile[0]
                    colIndex = currentTile[-1]

                    if (rowIndex == 0):
                        if (colIndex > 0):
                            if (grid[rowIndex][colIndex - 1] == "1"):
                                tempQueue.append((rowIndex, colIndex - 1))
                        if (colIndex < len(grid[0]) - 1):
                            if (grid[rowIndex][colIndex + 1] == "1"):
                                tempQueue.append((rowIndex, colIndex + 1))

                        if (rowIndex + 1 < len(grid) and grid[rowIndex + 1][colIndex] == "1"):
                            tempQueue.append((rowIndex + 1, colIndex))

                    elif (rowIndex == len(grid) - 1):
                        if (colIndex > 0):
                            if (grid[rowIndex][colIndex - 1] == "1"):
                                tempQueue.append((rowIndex, colIndex - 1))
                        if (colIndex < len(grid[0]) - 1):
                            if (grid[rowIndex][colIndex + 1] == "1"):
                                tempQueue.append((rowIndex, colIndex + 1))
                        if (grid[rowIndex - 1][colIndex] == "1"):
                            tempQueue.append((rowIndex - 1, colIndex))

                    elif (colIndex == 0):
                        if (grid[rowIndex - 1][colIndex] == "1"):
                            tempQueue.append((rowIndex - 1, colIndex))
                        if (colIndex + 1 < len(grid[0]) and grid[rowIndex][colIndex + 1] == "1"):
                            tempQueue.append((rowIndex, colIndex + 1))
                        if (grid[rowIndex + 1][colIndex] == "1"):
                            tempQueue.append((rowIndex + 1, colIndex))
                    
                    elif (colIndex == len(grid[0])-1):
                        if (grid[rowIndex - 1][colIndex] == "1"):
                            tempQueue.append((rowIndex - 1, colIndex))
                        if (grid[rowIndex][colIndex - 1] == "1"):
                            tempQueue.append((rowIndex, colIndex - 1))
                        if (grid[rowIndex + 1][colIndex] == "1"):
                            tempQueue.append((rowIndex + 1,colIndex))
                    else:
                        if (grid[rowIndex - 1][colIndex] == "1"):
                            tempQueue.append((rowIndex - 1, colIndex))
                        if (grid[rowIndex][colIndex - 1] == "1"):
                            tempQueue.append((rowIndex, colIndex - 1))
                        if (grid[rowIndex + 1][colIndex] == "1"):
                            tempQueue.append((rowIndex + 1, colIndex))
                        if (grid[rowIndex][colIndex + 1] == "1"):
                            tempQueue.append((rowIndex, colIndex + 1))
            if prevUsedLen != len(usedTiles): 
                IslandCount += 1
        return IslandCount
                

            
        