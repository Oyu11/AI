import random

# Define the graph structure with corrected city names
graph = {
    'nodes': ['Ulaanbaatar', 'Erdenet', 'Darkhan', 'Choibalsan', 'Mörön', 'Khovd', 'Ölgii', 'Bayankhongor', 'Dalanzadgad', 'Altai'],
    'edges': [
        ('Ulaanbaatar', 'Erdenet', {'weight': 231}),
        ('Ulaanbaatar', 'Darkhan', {'weight': 142}),
        ('Ulaanbaatar', 'Choibalsan', {'weight': 198}),
        ('Ulaanbaatar', 'Mörön', {'weight': 96}),
        ('Ulaanbaatar', 'Khovd', {'weight': 199}),
        ('Ulaanbaatar', 'Ölgii', {'weight': 218}),
        ('Ulaanbaatar', 'Bayankhongor', {'weight': 210}),
        ('Ulaanbaatar', 'Dalanzadgad', {'weight': 140}),
        ('Ulaanbaatar', 'Altai', {'weight': 297}),
        ('Erdenet', 'Darkhan', {'weight': 290}),
        ('Erdenet', 'Choibalsan', {'weight': 185}),
        ('Erdenet', 'Mörön', {'weight': 253}),
        ('Erdenet', 'Khovd', {'weight': 262}),
        ('Erdenet', 'Ölgii', {'weight': 242}),
        ('Erdenet', 'Bayankhongor', {'weight': 264}),
        ('Erdenet', 'Dalanzadgad', {'weight': 246}),
        ('Erdenet', 'Altai', {'weight': 186}),
        ('Darkhan', 'Choibalsan', {'weight': 151}),
        ('Darkhan', 'Mörön', {'weight': 93}),
        ('Darkhan', 'Khovd', {'weight': 85}),
        ('Darkhan', 'Ölgii', {'weight': 229}),
        ('Darkhan', 'Bayankhongor', {'weight': 157}),
        ('Darkhan', 'Dalanzadgad', {'weight': 221}),
        ('Darkhan', 'Altai', {'weight': 152}),
        ('Choibalsan', 'Mörön', {'weight': 56}),
        ('Choibalsan', 'Khovd', {'weight': 137}),
        ('Choibalsan', 'Ölgii', {'weight': 99}),
        ('Choibalsan', 'Bayankhongor', {'weight': 130}),
        ('Choibalsan', 'Dalanzadgad', {'weight': 126}),
        ('Choibalsan', 'Altai', {'weight': 55}),
        ('Mörön', 'Khovd', {'weight': 111}),
        ('Mörön', 'Ölgii', {'weight': 299}),
        ('Mörön', 'Bayankhongor', {'weight': 290}),
        ('Mörön', 'Dalanzadgad', {'weight': 260}),
        ('Mörön', 'Altai', {'weight': 231}),
        ('Khovd', 'Ölgii', {'weight': 150}),
        ('Khovd', 'Bayankhongor', {'weight': 115}),
        ('Khovd', 'Dalanzadgad', {'weight': 296}),
        ('Khovd', 'Altai', {'weight': 130}),
        ('Ölgii', 'Bayankhongor', {'weight': 232}),
        ('Ölgii', 'Dalanzadgad', {'weight': 299}),
        ('Ölgii', 'Altai', {'weight': 229}),
        ('Bayankhongor', 'Dalanzadgad', {'weight': 195}),
        ('Bayankhongor', 'Altai', {'weight': 262}),
        ('Dalanzadgad', 'Altai', {'weight': 263})
    ]
}

# Convert edges to an adjacency list for easy lookup
adj_list = {}
for edge in graph['edges']:
    node1, node2, data = edge
    weight = data['weight']
    
    if node1 not in adj_list:
        adj_list[node1] = []
    if node2 not in adj_list:
        adj_list[node2] = []
    
    adj_list[node1].append((node2, weight))
    adj_list[node2].append((node1, weight))

# Evaluation function: Path cost (sum of weights in a path)
def path_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        node = path[i]
        next_node = path[i + 1]
        for neighbor, weight in adj_list[node]:
            if neighbor == next_node:
                total_cost += weight
                break
    return total_cost

# Hill climbing search with a random start and return to start
def hill_climbing():
    start = random.choice(graph['nodes'])  # Random start city
    current_solution = [start]
    current_cost = float('inf')
    
    while len(current_solution) < len(graph['nodes']):
        last_node = current_solution[-1]
        neighbors = adj_list[last_node]
        
        # Randomly pick the next move with lower cost, avoiding already visited cities
        next_move = None
        next_cost = float('inf')
        
        for neighbor, weight in neighbors:
            if neighbor not in current_solution:  # Avoid revisiting cities
                potential_solution = current_solution + [neighbor]
                cost = path_cost(potential_solution)
                if cost < next_cost:
                    next_cost = cost
                    next_move = neighbor
        
        if next_move is None:
            break  # No valid moves found, stop the search
        
        current_solution.append(next_move)
        current_cost = next_cost
    
    # Return to the starting city
    current_solution.append(start)

    # Find the cost of returning to the starting city
    for neighbor, weight in adj_list[current_solution[-2]]:
        if neighbor == start:
            current_cost += weight
            break

    return current_solution, current_cost

# Example usage
solution, cost = hill_climbing()
print(f"Path found: {solution} with total cost {cost}")
