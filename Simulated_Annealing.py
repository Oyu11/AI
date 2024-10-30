import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes (cities)
nodes = ['Ulaanbaatar', 'Erdenet', 'Darkhan', 'Choibalsan', 'Mörön', 'Khovd', 'Ölgii', 'Bayankhongor', 'Dalanzadgad', 'Altai']

# Add edges (distances)
edges = [
    ('Ulaanbaatar', 'Erdenet', 231), ('Ulaanbaatar', 'Darkhan', 142), ('Ulaanbaatar', 'Choibalsan', 198),
    ('Ulaanbaatar', 'Mörön', 96), ('Ulaanbaatar', 'Khovd', 199), ('Ulaanbaatar', 'Ölgii', 218),
    ('Ulaanbaatar', 'Bayankhongor', 210), ('Ulaanbaatar', 'Dalanzadgad', 140), ('Ulaanbaatar', 'Altai', 297),
    ('Erdenet', 'Darkhan', 290), ('Erdenet', 'Choibalsan', 185), ('Erdenet', 'Mörön', 253),
    ('Erdenet', 'Khovd', 262), ('Erdenet', 'Ölgii', 242), ('Erdenet', 'Bayankhongor', 264),
    ('Erdenet', 'Dalanzadgad', 246), ('Erdenet', 'Altai', 186), ('Darkhan', 'Choibalsan', 151),
    ('Darkhan', 'Mörön', 93), ('Darkhan', 'Khovd', 85), ('Darkhan', 'Ölgii', 229),
    ('Darkhan', 'Bayankhongor', 157), ('Darkhan', 'Dalanzadgad', 221), ('Darkhan', 'Altai', 152),
    ('Choibalsan', 'Mörön', 56), ('Choibalsan', 'Khovd', 137), ('Choibalsan', 'Ölgii', 99),
    ('Choibalsan', 'Bayankhongor', 130), ('Choibalsan', 'Dalanzadgad', 126), ('Choibalsan', 'Altai', 55),
    ('Mörön', 'Khovd', 111), ('Mörön', 'Ölgii', 299), ('Mörön', 'Bayankhongor', 290),
    ('Mörön', 'Dalanzadgad', 260), ('Mörön', 'Altai', 231), ('Khovd', 'Ölgii', 150),
    ('Khovd', 'Bayankhongor', 115), ('Khovd', 'Dalanzadgad', 296), ('Khovd', 'Altai', 130),
    ('Ölgii', 'Bayankhongor', 232), ('Ölgii', 'Dalanzadgad', 299), ('Ölgii', 'Altai', 229),
    ('Bayankhongor', 'Dalanzadgad', 195), ('Bayankhongor', 'Altai', 262), ('Dalanzadgad', 'Altai', 263)
]

# Add edges with weights (distances)
G.add_weighted_edges_from(edges)



import random

# Function to calculate total distance of a route
def calculate_route_distance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i+1]]['weight']
    distance += graph[route[-1]][route[0]]['weight']  # Return to the starting city
    return distance

import math

# Simulated Annealing TSP
def simulated_annealing(graph, nodes, initial_temp, cooling_rate):
    current_route = nodes[:]
    random.shuffle(current_route)
    current_distance = calculate_route_distance(current_route, graph)
    
    temperature = initial_temp
    
    while temperature > 1:
        # Generate new neighboring route by swapping two cities
        new_route = current_route[:]
        i, j = random.sample(range(len(nodes)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        
        new_distance = calculate_route_distance(new_route, graph)
        
        # Decide if we should accept the new route
        if new_distance < current_distance:
            current_route = new_route
            current_distance = new_distance
        else:
            acceptance_probability = math.exp((current_distance - new_distance) / temperature)
            if random.random() < acceptance_probability:
                current_route = new_route
                current_distance = new_distance
        
        # Cool down
        temperature *= cooling_rate
    
    return current_route, current_distance



# Parameters
initial_temp = 10000
cooling_rate = 0.995

# Run Simulated Annealing
sa_route, sa_distance = simulated_annealing(G, nodes, initial_temp, cooling_rate)

# Print results
print(f"Simulated Annealing Route: {sa_route}, Distance: {sa_distance}")
