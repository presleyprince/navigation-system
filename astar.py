import heapq
import math
from search_algorithm import SearchAlgorithm

# A* (AS) - Viresh, Presley fixed and finished 
# Uses f(n) = g(n) + h(n) where:
#   g(n) = actual cost from origin to current node
#   h(n) = estimated cost from current node to nearest goal (Euclidean distance)
class AStarSearch(SearchAlgorithm):

    def __init__(self):
        super().__init__()
        #removed filename isnce search.py already calls it

    # removed heuristic method because, the base class already has it (search_algorithm)
    # wouldn't worek otherwise since self.Nodes is a list of strings

    def search(self):
        # Each heap entry: (f, g, node, path_so_far)
        # f = g + h, g = cost so far, node = current node
        self.node_positions = self.build_node_positions() # search_algorithm needs self.node_positions so added before it's calculating distances
        start_h = self.heuristic(self.Origin)
        counter = 0 # added to avoid crashing when paths are compared
        heap = [(start_h, 0, counter, self.Origin, [self.Origin])] # added counter since it is the first item added to the heap (needing an identifier number)

        # Best g-cost seen for each node (to skip worse paths)
        best_g = {self.Origin: 0}

        node_count = 0

        while heap:
            f, g, _, current_node, path = heapq.heappop(heap) # added _ so python won't crash when two paths have equal cost

            node_count += 1

            # Skip if we've already found a cheaper route to this node
            if g > best_g.get(current_node, float('inf')):
                continue

            if current_node in self.Goal:
                return current_node, node_count, path

            # Expand neighbors
            neighbors = []
            for edge in self.Edges:
                if not edge.strip(): # file has blank lines at end so skip the empty lines
                    continue
                src, dst, cost = self.format_edge(edge) # self.edge is a list not a dictionary that uses strings
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
                    counter += 1 # added counter so eevry item that is added to the heap has a unique number, avoiding two entries being identical
                    heapq.heappush(heap, (new_f, new_g, counter, neighbor, path + [neighbor])) # added counter cause new items get added here to the heap, needing unique numbers to avoid crashing if paths have the same costs

        return None, node_count, []  # No path found

    def run_algorithm(self):
        goal_node, node_count, path = self.search()
        return node_count, path
    #removed printing logic since search.py already does
