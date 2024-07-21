### Problem 1

#Rotting Oranges(https://leetcode.com/problems/rotting-oranges)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        q = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        time = 0
        while fresh > 0 and q:
            size = len(q)
            time += 1
            for i in range(size):
                current = q.popleft()
                r, c = current

                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc

                    if nr >= 0 and nc >= 0 and nr < m and nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1

        if fresh == 0:
            return time 
        else:
            return -1