import csv
import heapq

def build_graph(filename):
    graph = {}

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            src = row['source']
            dest = row['destination']
            dist = int(row['distance'])

            # add both directions (undirected graph)
            if src not in graph:
                graph[src] = []
            if dest not in graph:
                graph[dest] = []

            graph[src].append((dest, dist))
            graph[dest].append((src, dist))

    return graph


def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node]:
            new_dist = curr_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


graph = build_graph("Indian_cities.csv")

start = input("Enter source city: ")

if start not in graph:
    print("City not found!")
else:
    result = dijkstra(graph, start)

    print(f"\nShortest distances from {start}:\n")
    for city in result:
        print(f"{city} -> {result[city]} km")