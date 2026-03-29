from collections import deque


# --8<-- [start:max_area_of_island_dfs]
def max_area_of_island_dfs(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    def is_safe(i: int, j: int) -> bool:
        return (
                0 <= i < len(grid) and
                0 <= j < len(grid[0]) and
                grid[i][j] == 1
        )

    def explore(i: int, j: int) -> int:
        if not is_safe(i, j):
            return 0

        grid[i][j] = 0  # Mark as 'visited'

        return (
                1 +
                explore(i + 1, j) +
                explore(i - 1, j) +
                explore(i, j + 1) +
                explore(i, j - 1)
        )

    max_size = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                max_size = max(explore(i, j), max_size)

    return max_size


# --8<-- [end:max_area_of_island_dfs]

# --8<-- [start:max_area_of_island_bfs]
def max_area_of_island_bfs(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def explore(i: int, j: int):
        queue = deque()
        queue.append((i, j))
        grid[i][j] = 0
        size = 1

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = '0'
                    queue.append((nx, ny))
                    size += 1
        return size

    max_size = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                max_size = max(explore(i, j), max_size)

    return max_size


# --8<-- [end:max_area_of_island_bfs]

g = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]

print(max_area_of_island_dfs(g))

g = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]

print(max_area_of_island_bfs(g))
