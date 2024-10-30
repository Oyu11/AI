import heapq

# Romania map graph representation
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99},
    'Hirsova': {'Urziceni': 98},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97},
    'Rimnicu': {'Sibiu': 80},
    'Urziceni': {'Vaslui': 142}
}

# Make the graph bidirectional
def make_graph_bidirectional(graph):
    new_graph = {city: connections.copy() for city, connections in graph.items()}
    for city, connections in graph.items():
        for neighbor, distance in connections.items():
            if neighbor not in new_graph:
                new_graph[neighbor] = {}
            new_graph[neighbor][city] = distance
    return new_graph

romania_map_bidirectional = make_graph_bidirectional(romania_map)

def dfs(graph, start, goal):
    stack = [(start, [start], 0)]  
    visited = set()  
    while stack:
        (city, path, cost) = stack.pop()
        if city == goal:
            return path, cost
        if city not in visited:
            visited.add(city)
            for neighbor, distance in graph.get(city, {}).items():
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + distance))
    return None, None

def bfs(graph, start, goal):
    queue = [(start, [start], 0)]  
    visited = set()  
    while queue:
        (city, path, cost) = queue.pop(0)
        if city == goal:
            return path, cost
        if city not in visited:
            visited.add(city)
            for neighbor, distance in graph.get(city, {}).items():
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + distance))
    return None, None

def ucs(graph, start, goal):
    priority_queue = [(0, start, [start])]  
    visited = set()  
    while priority_queue:
        (cost, city, path) = heapq.heappop(priority_queue)  
        if city == goal:
            return path, cost  
        if city not in visited:
            visited.add(city)  
            for neighbor, distance in graph.get(city, {}).items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost + distance, neighbor, path + [neighbor]))
    return None, None  

dfs_path, dfs_cost = dfs(romania_map_bidirectional, 'Arad', 'Bucharest')
bfs_path, bfs_cost = bfs(romania_map_bidirectional, 'Arad', 'Bucharest')
ucs_path, ucs_cost = ucs(romania_map_bidirectional, 'Arad', 'Bucharest')

# Print the results
print("DFS Path:", dfs_path, "Total Distance:", dfs_cost)  
print("BFS Path:", bfs_path, "Total Distance:", bfs_cost) 
print("UCS Path:", ucs_path, "Total Distance:", ucs_cost)  
