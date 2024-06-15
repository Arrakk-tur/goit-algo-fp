import heapq


def dijkstra(grph, start):
    # Ініціалізація
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    dists = {vert: float('inf') for vert in grph}
    dists[start] = 0
    shortest_path_tree_set = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in shortest_path_tree_set:
            continue

        shortest_path_tree_set.add(current_vertex)

        for neighbor, weight in grph[current_vertex]:
            dist = current_distance + weight

            if dist < dists[neighbor]:
                dists[neighbor] = dist
                heapq.heappush(priority_queue, (dist, neighbor))

    return dists


# Приклад графа
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Виклик функції
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

# Виведення результату
print("Найкоротші відстані від вершини", start_vertex, "до всіх інших вершин:")
for vertex, distance in distances.items():
    print(f"Вершина {vertex}: відстань {distance}")
