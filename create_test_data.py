# Not part of the assignment, made to generate test cases.

import random
import os
from collections import deque

def bfs_distance(graph, start, end):
    """Calculate shortest path distance (number of hops) using BFS."""
    if start == end:
        return 0
    
    visited = {start}
    queue = deque([(start, 0)])
    
    
    while queue:
        node, distance = queue.popleft()
        
        if node in graph:
            for neighbor in graph[node]:
                if neighbor == end:
                    return distance + 1
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance + 1))
    
    return float('inf')  # No path found

def suggest_edges(num_nodes, num_edges_tried, min_distance):
    """Suggest appropriate edge count for desired minimum distance."""
    import math
    
    min_for_connectivity = num_nodes - 1
    
    # Calculate average degree from attempted edges
    avg_degree = (2 * num_edges_tried) / num_nodes
    
    # In random graphs, average shortest path ≈ log(n) / log(avg_degree)
    # Higher density = shorter paths. We need sparser graphs for longer paths.
    current_avg_path = math.log(num_nodes) / math.log(max(avg_degree, 2))
    
    # Estimate: to achieve min_distance, try much sparser graph
    # With degree d, avg path ≈ log(n)/log(d), so solve for target distance
    # If we want paths of length min_distance:
    # min_distance ≈ log(n) / log(d), so d ≈ exp(log(n) / min_distance)
    target_degree = max(2, math.exp(math.log(num_nodes) / min_distance))
    recommended_edges = max(min_for_connectivity, int(target_degree * num_nodes / 2))
    
    return min_for_connectivity, recommended_edges, current_avg_path

def create_test_file(num_nodes, num_edges, num_destinations=1, max_coord=20, min_cost=1, max_cost=10, min_distance=1, filename=None):
    """
    Creates a test data file in the PathFinder format.
    
    Args:
        num_nodes: Number of nodes to generate
        num_edges: Number of edges to generate
        num_destinations: Number of destination nodes (default: 1)
        max_coord: Maximum coordinate value (default: 20)
        min_cost: Minimum edge cost (default: 1)
        max_cost: Maximum edge cost (default: 10)
        min_distance: Minimum hop distance between origin and destinations (default: 1)
        filename: Output filename (default: PathFinder-test-random.txt)
    """
    
    if filename is None:
        filename = "PathFinder-test-random.txt"
    
    # Validate inputs
    if num_nodes < 2:
        print("Error: Number of nodes must be at least 2")
        return False
    
    if num_destinations >= num_nodes:
        print(f"Error: Number of destinations must be less than number of nodes")
        return False
    
    max_possible_edges = num_nodes * (num_nodes - 1)  # Maximum undirected edges
    if num_edges > max_possible_edges:
        print(f"Error: Maximum possible edges for {num_nodes} nodes is {max_possible_edges}")
        return False
    
    # Generate random node coordinates
    nodes = {}
    for i in range(1, num_nodes + 1):
        x = random.randint(1, max_coord)
        y = random.randint(1, max_coord)
        nodes[i] = (x, y)
    
    # Generate random edges without duplicates
    edges = set()
    edge_list = []
    
    while len(edges) < num_edges:
        node1 = random.randint(1, num_nodes)
        node2 = random.randint(1, num_nodes)
        
        # Ensure different nodes and no duplicate edges (considering both directions)
        if node1 == node2:
            continue
        
        edge_pair = tuple(sorted([node1, node2]))
        if edge_pair in edges:
            continue
        
        edges.add(edge_pair)
        cost = random.randint(min_cost, max_cost)
        edge_list.append((node1, node2, cost))
    
    # Select random origin and destinations
    all_nodes = list(range(1, num_nodes + 1))
    origin = random.choice(all_nodes)
    
    # Build adjacency graph for distance checking
    graph = {node: [] for node in range(1, num_nodes + 1)}
    for node1, node2, cost in edge_list:
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    # Select destinations that meet minimum distance requirement
    available_destinations = [n for n in all_nodes if n != origin]
    destinations = []
    max_attempts = 100
    attempts = 0
    
    while len(destinations) < num_destinations and attempts < max_attempts:
        candidate = random.choice(available_destinations)
        distance = bfs_distance(graph, origin, candidate)
        
        if distance >= min_distance and candidate not in destinations:
            destinations.append(candidate)
        
        attempts += 1
    
    if len(destinations) < num_destinations:
        print(f"Warning: Could only find {len(destinations)} destinations with minimum distance of {min_distance}")
        if len(destinations) == 0:
            min_edges, recommended_edges, avg_path = suggest_edges(num_nodes, num_edges, min_distance)
            print(f"Error: Could not find any valid destinations.")
            print(f"\nGraph Analysis for {num_nodes} nodes with {num_edges} edges:")
            print(f"  - Average degree: {(2 * num_edges) / num_nodes:.2f}")
            print(f"  - Estimated average shortest path: {avg_path:.2f} hops")
            print(f"  - Your graph is TOO DENSE for min_distance={min_distance}")
            print(f"\nSuggested edge counts to achieve min_distance={min_distance}:")
            print(f"  - Minimum (just connected): {min_edges} edges")
            print(f"  - Recommended (sparser): ~{recommended_edges} edges")
            print(f"\nNote: Shorter paths occur in denser graphs. Try reducing num_edges or increasing min_distance tolerance.")
            return False
    
    # Write to file
    try:
        with open(filename, 'w') as f:
            # Write nodes
            f.write("Nodes:\n")
            for node_id in sorted(nodes.keys()):
                x, y = nodes[node_id]
                f.write(f"{node_id}: ({x},{y})\n")
            
            # Write edges
            f.write("Edges:\n")
            for node1, node2, cost in edge_list:
                # Write both directions for undirected graph
                f.write(f"({node1},{node2}): {cost}\n")
                f.write(f"({node2},{node1}): {cost}\n")
            
            # Write origin
            f.write("Origin:\n")
            f.write(f"{origin}\n")
            
            # Write destinations
            f.write("Destinations:\n")
            destinations_str = "; ".join(map(str, destinations))
            f.write(f"{destinations_str}\n")
        
        print(f"✓ Successfully created '{filename}'")
        print(f"  - Nodes: {num_nodes}")
        print(f"  - Edges: {num_edges} (bidirectional, so {num_edges * 2} total edge entries)")
        print(f"  - Origin: {origin}")
        print(f"  - Destinations: {destinations}")
        
        # Print distances for verification
        for dest in destinations:
            distance = bfs_distance(graph, origin, dest)
            print(f"    Distance from {origin} to {dest}: {distance} hops")
        return True
    
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False


def interactive_create():
    """Interactive mode for creating test files."""
    print("\n=== PathFinder Test File Generator ===\n")
    
    try:
        num_nodes = int(input("Number of nodes: "))
        num_edges = int(input("Number of edges: "))
        num_destinations = int(input("Number of destinations (default 1): ") or "1")
        max_coord = int(input("Maximum coordinate value (default 20): ") or "20")
        min_cost = int(input("Minimum edge cost (default 1): ") or "1")
        max_cost = int(input("Maximum edge cost (default 10): ") or "10")
        min_distance = int(input("Minimum hop distance between origin and destinations (default 1): ") or "1")
        filename = input("Output filename (default PathFinder-test-random.txt): ").strip()
        
        if not filename:
            filename = "PathFinder-test-random.txt"
        
        create_test_file(
            num_nodes=num_nodes,
            num_edges=num_edges,
            num_destinations=num_destinations,
            max_coord=max_coord,
            min_cost=min_cost,
            max_cost=max_cost,
            min_distance=min_distance,
            filename=filename
        )
    
    except ValueError:
        print("Error: Please enter valid numbers")
        return False
    except KeyboardInterrupt:
        print("\n\nCancelled.")
        return False
    
    return True


if __name__ == "__main__":
    interactive_create()
