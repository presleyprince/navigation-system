import heapq
import math
from search_algorithm import SearchAlgorithm

# A* (AS) - Viresh
# Uses f(n) = g(n) + h(n) where:
#   g(n) = actual cost from origin to current node
#   h(n) = estimated cost from current node to nearest goal (Euclidean distance)
class AStarSearch(SearchAlgorithm):

    def __init__(self, filename):
        super().__init__()
        self.read_file(filename)

    def heuristic(self, node):
        """Euclidean distance from node to the nearest goal node."""
        x1, y1 = self.Nodes[node]
        return min(
            math.sqrt((x1 - self.Nodes[goal][0])**2 + (y1 - self.Nodes[goal][1])**2)
            for goal in self.Goal
        )

    def search(self):
        # Each heap entry: (f, g, node, path_so_far)
        # f = g + h, g = cost so far, node = current node
        start_h = self.heuristic(self.Origin)
        heap = [(start_h, 0, self.Origin, [self.Origin])]

        # Best g-cost seen for each node (to skip worse paths)
        best_g = {self.Origin: 0}

        node_count = 0

        while heap:
            f, g, current_node, path = heapq.heappop(heap)

            node_count += 1

            # Skip if we've already found a cheaper route to this node
            if g > best_g.get(current_node, float('inf')):
                continue

            if current_node in self.Goal:
                return current_node, node_count, path

            # Expand neighbors
            neighbors = []
            for (src, dst), cost in self.Edges.items():
                if src == current_node:
                    neighbors.append((dst, cost))

            # Sort by node ID ascending so equal-cost nodes expand in order (spec requirement)
            neighbors.sort(key=lambda x: x[0])

            for neighbor, edge_cost in neighbors:
                new_g = g + edge_cost
                if new_g < best_g.get(neighbor, float('inf')):
                    best_g[neighbor] = new_g
                    new_h = self.heuristic(neighbor)
                    new_f = new_g + new_h
                    heapq.heappush(heap, (new_f, new_g, neighbor, path + [neighbor]))

        return None, node_count, []  # No path found

    def run_algorithm(self):
        goal_node, node_count, path = self.search()
        if path:
            print(f"{self.filename} AS")
            print(f"{goal_node} {node_count}")
            print(" -> ".join(str(n) for n in path))
        else:
            print(f"{self.filename} AS")
            print("No path found")
