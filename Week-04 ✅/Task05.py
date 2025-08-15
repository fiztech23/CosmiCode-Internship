# Week-04/Task05.py
# Task 5: Write a program to find the shortest path in a graph
# using Dijkstra's algorithm.
print("=== TASK #5 OUTPUT ===")

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'B': 1, 'D': 8},
    'D': {}
}

def dijkstra(graph, start):
    distances = {}
    for node in graph:
        distances[node] = float('inf')
    distances[start] = 0
    visited = []
    while len(visited) < len(graph):
        min_node = None
        for node in graph:
            if node not in visited:
                if min_node is None or distances[node] < distances[min_node]:
                    min_node = node
        for neighbor in graph[min_node]:
            new_distance = distances[min_node] + graph[min_node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

        visited.append(min_node)
    return distances

print(f"The shortest path is: {dijkstra(graph, 'A')}")

