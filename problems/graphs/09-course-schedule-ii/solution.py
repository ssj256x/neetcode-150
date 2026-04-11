# --8<-- [start:find_order]
def find_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = {i: [] for i in range(num_courses)}

    for course, pre in prerequisites:
        graph[course].append(pre)

    state = [0] * num_courses  # 0 = unprocessed, 1 = visiting, 2 = done
    order = []

    def dfs(course):
        if state[course] == 1:
            return False
        if state[course] == 2:
            return True

        state[course] = 1

        for pre in graph[course]:
            if not dfs(pre):
                return False

        state[course] = 2
        order.append(course)
        return True

    for i in range(num_courses):
        if not dfs(i):
            return []

    return order


# --8<-- [end:find_order]

p = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [3, 4]
]

print(find_order(5, p))
