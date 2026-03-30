from search_algorithm import SearchAlgorithm
import heapq

class DijkstraSearch(SearchAlgorithm):
    
    def __init__(self):
        super().__init__()
        self.queue = []
        self.visited = set()
        self.parent = {}
        self.explored_count = 0
        self.cost = {}
        
    def search(self, node):
        # Get Node ID from the node entry
        node_id = self.node_id(node)
        current_cost = self.cost[node_id]

        # Explore the neighbors of the current node by iterating through the edges and checking for connections
        for edge in self.Edges:
            if ":" not in edge:
                continue

            current_node, next_node, cost = self.format_edge(edge)
            if current_node != node_id:
                continue
            elif next_node in self.visited:
                continue

            new_cost = current_cost + cost

            if next_node not in self.parent or new_cost < self.cost[next_node]:
                self.cost[next_node] = new_cost
                self.parent[next_node] = node_id
                heapq.heappush(self.queue, (new_cost, next_node))  # Add the next node to the priority queue with its distance as the priority

    def run_algorithm(self):
        # For Kyle to do
        pass