from collections import deque


# --8<-- [start:num_islands_dfs]
def num_islands_dfs(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    def is_safe(i: int, j: int) -> bool:
        return (
                0 <= i < len(grid) and
                0 <= j < len(grid[0]) and
                grid[i][j] == '1'
        )

    def explore(i: int, j: int):
        if not is_safe(i, j):
            return

        grid[i][j] = '0'  # Mark as 'visited'

        explore(i + 1, j)
        explore(i - 1, j)
        explore(i, j + 1)
        explore(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                explore(i, j)
                count += 1

    return count


# --8<-- [end:num_islands_dfs]

# --8<-- [start:num_islands_bfs]
def num_islands_bfs(grid: list[list[str]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def explore(i: int, j: int):
        queue = deque()
        queue.append((i, j))
        grid[i][j] = '0'

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                explore(i, j)
                count += 1

    return count


# --8<-- [end:num_islands_bfs]

g = [
    ["1", "1", "0", "0", "1"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print(num_islands_dfs(g[:]))

g = [
    ["1", "1", "0", "0", "1"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(num_islands_bfs(g))
