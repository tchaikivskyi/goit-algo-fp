import heapq

class Graph:
    def __init__(self):
        self.edges = {}  

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  
    def dijkstra(self, start):
        distances = {node: float('inf') for node in self.edges}
        distances[start] = 0
        visited = set()
        priority_queue = [(0, start)]  

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbor, weight in self.edges[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


g = Graph()
g.add_edge("A", "B", 4)
g.add_edge("A", "C", 2)
g.add_edge("B", "C", 5)
g.add_edge("B", "D", 10)
g.add_edge("C", "E", 3)
g.add_edge("E", "D", 4)
g.add_edge("D", "F", 11)

start_node = "A"
shortest_paths = g.dijkstra(start_node)

print(f"Найкоротші шляхи від вершини {start_node}:")
for node, distance in shortest_paths.items():
    print(f"До вершини {node} = {distance}")
