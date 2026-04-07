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

    def run_algorithm(self): # Dijkstra's algorithm implementation using a priority queue (min-heap) to explore nodes based on the lowest cumulative cost from the origin
        if self.Origin is None:
            return (0, [])

        self.queue = [] # Priority queue to explore nodes based on the lowest cumulative cost from the origin
        self.visited = set() # Set to keep track of visited nodes to avoid re-exploration
        self.parent = {self.Origin: None} # Dictionary to track the parent of each node for path reconstruction, starting with the origin having no parent
        self.cost = {self.Origin: 0} # Dictionary to track the cumulative cost from the origin to each node, starting with the origin having a cost of 0
        self.explored_nodes = [] # List to keep track of explored nodes for counting purposes

        heapq.heappush(self.queue, (0, self.Origin)) # Add the origin node to the priority queue with a cost of 0

        while self.queue:
            current_cost, current_node = heapq.heappop(self.queue) # Get the next node to explore from the priority queue, which will be the node with the lowest cumulative cost from the origin

            if current_node in self.visited: # If the current node has already been visited, skip it to avoid re-exploration
                continue

            # Ignore stale queue entries that are no longer optimal.
            if current_cost > self.cost.get(current_node, float("inf")):
                continue

            self.visited.add(current_node) # Mark the current node as visited to avoid re-exploration
            self.explored_nodes.append(current_node) # Add the current node to the list of explored nodes for counting purposes

            if current_node in self.Goal: # If the current node is a goal node, reconstruct the path from the origin to the goal and return the number of nodes explored and the path taken
                path = self.reconstruct_path(current_node) # Reconstruct the path from the origin to the goal using the parent dictionary
                return (len(self.explored_nodes), path) # Return the number of nodes explored and the path taken to reach the goal

            self.search(current_node) # Explore the current node and add its neighbors to the priority queue based on their cumulative cost from the origin

        return (len(self.explored_nodes), []) # If the priority queue is empty and no goal was found, return the number of nodes explored and an empty path