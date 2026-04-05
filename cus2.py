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
        if self.Origin is None:
            return (0, [])

        self.queue = []
        self.visited = set()
        self.parent = {self.Origin: None}
        self.cost = {self.Origin: 0}
        self.explored_nodes = []

        heapq.heappush(self.queue, (0, self.Origin))

        while self.queue:
            current_cost, current_node = heapq.heappop(self.queue)

            if current_node in self.visited:
                continue

            # Ignore stale queue entries that are no longer optimal.
            if current_cost > self.cost.get(current_node, float("inf")):
                continue

            self.visited.add(current_node)
            self.explored_nodes.append(current_node)

            if current_node in self.Goal:
                path = self.reconstruct_path(current_node)
                return (len(self.explored_nodes), path)

            self.search(current_node)

        return (len(self.explored_nodes), [])