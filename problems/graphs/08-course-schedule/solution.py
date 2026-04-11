def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}

    for course, pre in prerequisites:
        graph[course].append(pre)

    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if graph[course] == []:
            return True

        visited.add(course)

        for pre in graph[course]:
            if not dfs(pre):
                return False

        visited.remove(course)
        graph[course] = []
        return True

    for i in range(num_courses):
        if not dfs(i):
            return False

    return True


# --8<-- [start:can_finish]
def can_finish_with_state(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}

    for course, pre in prerequisites:
        graph[course].append(pre)

    state = [0] * num_courses  # 0=unvisited, 1=visiting, 2=done

    def dfs(course):
        if state[course] == 1:
            return False  # cycle
        if state[course] == 2:
            return True  # already processed

        state[course] = 1  # mark visiting

        for pre in graph[course]:
            if not dfs(pre):
                return False

        state[course] = 2  # mark done
        return True

    for i in range(num_courses):
        if not dfs(i):
            return False

    return True


# --8<-- [end:can_finish]

p = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [3, 4]
]

print(can_finish(5, p))
