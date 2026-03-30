from search_algorithm import SearchAlgorithm
import heapq

class DijkstraSearch(SearchAlgorithm):
    
    def __init__(self):
        super().__init__()
        self.queue = []
        self.visited = set()
        self.parent = {}
        self.explored_count = 0
        self.distance = {}
        
    def search(self, node):
        # Get Node ID from the node entry
        node_id = self.node_id(node)
        current_distance = self.distance[node_id]

        # Explore the neighbors of the current node by iterating through the edges and checking for connections
        for edge in self.Edges:
            if ":" not in edge:
                continue

            current_node, next_node, cost = self.format_edge(edge)
            if current_node != node_id:
                continue
            elif next_node in self.visited:
                continue

            new_distance = current_distance + cost

            if next_node not in self.parent or new_distance < self.distance[next_node]:
                self.distance[next_node] = new_distance
                self.parent[next_node] = node_id
                heapq.heappush(self.queue, (new_distance, next_node))  # Add the next node to the priority queue with its distance as the priority

    def run_algorithm(self):
        # For Kyle to do
        pass