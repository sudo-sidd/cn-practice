# Experiment 13: Bellman-Ford Algorithm
def bellman_ford(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Check for negative weight cycles
    for u in graph:
        for v, weight in graph[u].items():
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                print("Graph contains negative weight cycle")
                return None

    return distance

if __name__ == '__main__':
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2, 'E': 2},
        'C': {},
        'D': {'B': 1, 'C': 5},
        'E': {'D': -3}
    }
    start_node = 'A'
    distances = bellman_ford(graph, start_node)
    if distances:
        print(f"Shortest distances from {start_node}: {distances}")
