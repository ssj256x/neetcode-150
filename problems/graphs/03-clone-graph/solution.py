from collections import deque
from typing import Optional


# --8<-- [start:node]
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f'Node({self.val=}, {self.neighbors=})'


# --8<-- [end:node]

# --8<-- [start:clone_graph_dfs]
def clone_graph_dfs(node: Optional['Node']) -> Optional['Node']:
    def dfs(cur: Node) -> Node:
        if cur in old_new:
            return old_new[cur]

        cloned = Node(cur.val)
        old_new[cur] = cloned

        for n in cur.neighbors:
            cloned.neighbors.append(dfs(n))

        return cloned

    old_new = {}
    return dfs(node)


# --8<-- [end:clone_graph_dfs]

# --8<-- [start:clone_graph_bfs]
def clone_graph_bfs(node: 'Node') -> 'Node':
    if not node:
        return None

    old_to_new = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()

        for nei in curr.neighbors:
            if nei not in old_to_new:
                old_to_new[nei] = Node(nei.val)
                queue.append(nei)

            old_to_new[curr].neighbors.append(old_to_new[nei])

    return old_to_new[node]


# --8<-- [end:clone_graph_bfs]

# Build graph manually
def build_graph():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    return n1


# Print graph (DFS traversal)
def print_graph(node):
    visited = set()

    def dfs(curr):
        if curr in visited:
            return
        visited.add(curr)

        print(f"Node {curr.val} -> {[n.val for n in curr.neighbors]}")

        for nei in curr.neighbors:
            dfs(nei)

    dfs(node)


# Verify deep copy
def verify_clone(original, clone):
    visited = set()

    def dfs(o, c):
        if o in visited:
            return True

        visited.add(o)

        # Values must match
        if o.val != c.val:
            return False

        # Objects must be different
        if o is c:
            return False

        # Same number of neighbors
        if len(o.neighbors) != len(c.neighbors):
            return False

        for i in range(len(o.neighbors)):
            if not dfs(o.neighbors[i], c.neighbors[i]):
                return False

        return True

    return dfs(original, clone)


# ---- Run Test ----

original = build_graph()

print("Original Graph:")
print_graph(original)

cloned = clone_graph_dfs(original)  # your function

print("\nCloned Graph:")
print_graph(cloned)

print("\nIs Deep Copy Valid?", verify_clone(original, cloned))
