#Task 1
"""
Modify the 'depth-first search' to produce strongly connected components (Strongly Connected Components ).
"""

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


