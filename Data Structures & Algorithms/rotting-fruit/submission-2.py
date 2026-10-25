from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        seen = set()
        tempQueue = deque();
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 2):
                    tempQueue.append((r, c))

        nextQueue = deque()
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1))
        if (tempQueue):
            time -= 1
        while (tempQueue):
            print(tempQueue)

            r, c = tempQueue.popleft()
            if (r, c) in seen:
                continue
            seen.add((r,c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    nextQueue.append((nr, nc))
            if (len(tempQueue) == 0):
                time += 1
                tempQueue = nextQueue
                nextQueue = deque()

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c]) == 1:
                    return -1
        return time
