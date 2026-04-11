def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []

    m, n = len(heights), len(heights[0])

    pacific = set()
    atlantic = set()

    def dfs(i: int, j: int, visited: set, prev_height: int):
        # Guard clause
        if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                (i, j) in visited or
                heights[i][j] < prev_height
        ):
            return

        visited.add((i, j))

        # Explore all 4 directions blindly
        dfs(i + 1, j, visited, heights[i][j])
        dfs(i - 1, j, visited, heights[i][j])
        dfs(i, j + 1, visited, heights[i][j])
        dfs(i, j - 1, visited, heights[i][j])

    # Pacific
    for i in range(m):
        dfs(i, 0, pacific, heights[i][0])
    for j in range(n):
        dfs(0, j, pacific, heights[0][j])

    # Atlantic
    for i in range(m):
        dfs(i, n - 1, atlantic, heights[i][n - 1])
    for j in range(n):
        dfs(m - 1, j, atlantic, heights[m - 1][j])

    # Intersection
    res = []
    for i in range(m):
        for j in range(n):
            if (i, j) in pacific and (i, j) in atlantic:
                res.append([i, j])

    return res
