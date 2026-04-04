from collections import deque

# --8<-- [start:islands_and_treasure]
def islands_and_treasure(grid: list[list[int]]) -> None:
    if not grid:
        return

    m, n = len(grid), len(grid[0])
    queue = deque()
    inf = 2 ** 31 - 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == inf:
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))
# --8<-- [end:islands_and_treasure]

I = 2 ** 31 - 1
X = -1
i = [
    [I, X, 0, I],
    [I, I, I, X],
    [I, X, I, X],
    [0, X, I, I]
]
islands_and_treasure(i)
print(i)
