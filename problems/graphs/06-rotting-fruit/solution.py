from collections import deque


# --8<-- [start:oranges_rotting]
def oranges_rotting(grid: list[list[int]]) -> int:
    queue = deque()
    m, n = len(grid), len(grid[0])
    fresh = 0
    time = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            if grid[i][j] == 1:
                fresh += 1

    while queue and fresh > 0:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    queue.append((nx, ny))
        time += 1

    return time if fresh == 0 else -1


# --8<-- [end:oranges_rotting]

g = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
print(oranges_rotting(g))
g = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
print(oranges_rotting(g))
