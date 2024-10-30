	
#DFS, BFS, UCS алгоритмуудыг хэрэгжүүлж Arad хотоос Bucharest хот хүртэлх замыг ол. Алгоритмыг харьцуулах үүднээс шийд олдтол явсан бүх хотуудын замын нийлбэрийг бодож гарна.

romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))
 



def dfs(graph, start):
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Use a stack to manage the frontier
    
    while stack:
        node = stack.pop()  # Get the last inserted node (LIFO)
        
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            
            # Add unvisited neighbors to the stack
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage
graph = {
    'Arad': ['Zerlind', 'Sibiu', 'Timisoara'],
    'Bucharest': ['Urzicent', 'Pitesti', 'Giurgiu','Fegaras'],
    'Craiova': ['Drobeta','Rimnicu','Pitest'],
    'D': [],
    'E': [],
    'F': []
}

dfs(graph, 'A')


from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Use a queue to manage the frontier
    
    while queue:
        node = queue.popleft()  # Get the first inserted node (FIFO)
        
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)
            
            # Add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

bfs(graph, 'A')


import heapq

def ucs(graph, start, goal):
    pq = []  # Priority queue to store (cost, node)
    heapq.heappush(pq, (0, start))  # Push the start node with cost 0
    visited = set()  # Keep track of visited nodes
    costs = {start: 0}  # Store the cost of reaching each node
    
    while pq:
        cost, node = heapq.heappop(pq)  # Get the node with the lowest cost
        
        if node == goal:
            return cost  # Return the cost when the goal is reached
        
        if node not in visited:
            visited.add(node)
            
            # Check all neighbors
            for neighbor, weight in graph[node]:
                new_cost = cost + weight  # Compute the cost to the neighbor
                
                if neighbor not in costs or new_cost < costs[neighbor]:
                    costs[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))  # Add the neighbor with its updated cost

    return float('inf')  # If the goal is unreachable

# Example usage
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [],
    'E': [],
    'F': []
}

result = ucs(graph, 'A', 'F')
print("Cost from A to F:", result)
