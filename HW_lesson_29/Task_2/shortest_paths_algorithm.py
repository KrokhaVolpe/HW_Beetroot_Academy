#Task 2
"""
Using breadth-first search write an algorithm that can determine the shortest path from each vertex to every other vertex.
This is called the all-pairs shortest path problem.
"""

from collections import deque

def bfs(graph, start):
    level = {vertex: -1 for vertex in graph}
    level[start] = 0

    queue = deque([start])

    while queue:
        current = queue.popleft()

        for i, _ in graph[current]:
            if level[i] == -1:
                queue.append(i)
                level[i] = level[current] + 1

    return level


