# Kyle, Jake

import heapq
from search_algorithm import SearchAlgorithm

class GreedyBestFirstSearch(SearchAlgorithm):
    def __init__(self):
        # Intializing the variables, from parent and needed gbfs specific variables
        super().__init__()
        self.queue = []
        self.visited = set()
        self.parent = {}
        self.explored_count = 0

    def search(self, node):
        # Get Node ID from the node entry
        node_id = self.node_id(node)

        # Explore the neighbors of the current node by iterating through the edges and checking for connections
        for edge in self.Edges:
            if ":" not in edge:
                continue

            current_node, next_node, cost = self.format_edge(edge)
            if current_node != node_id:
                continue
            elif next_node in self.visited:
                continue
            elif next_node not in self.parent:
                self.parent[next_node] = node_id

            heapq.heappush(self.queue, (self.heuristic(next_node), next_node))  # Add the next node to the priority queue with its heuristic value as the priority

    def run_algorithm(self):
        if self.Origin is None:
            return (0, [])  # No origin node defined, cannot run the algorithm
            
        self.queue = []
        self.visited = set()
        self.parent = {self.Origin: None}  # The origin node has no parent
        self.explored_nodes = []  # List to keep track of explored nodes
        self.node_positions = self.build_node_positions()

        heapq.heappush(self.queue, (self.heuristic(self.Origin), self.Origin))  # Start with the origin node in the priority queue with a cost of 0

        while self.queue:
            current_node = heapq.heappop(self.queue)[1]  # Get the next node to explore from the priority queue

            if current_node in self.visited:
                continue

            self.visited.add(current_node)  # Mark the current node as visited
            self.explored_nodes.append(current_node)  # Add the current node to the list of explored nodes
                
            if current_node in self.Goal:
                path = self.reconstruct_path(current_node)  # Reconstruct the path from the origin to the goal
                return (len(self.explored_nodes), path)  # Return the number of nodes explored and the path taken
                
            self.search(current_node)  # Explore the current node and add its neighbors to the queue

        return (len(self.explored_nodes), [])  # If the queue is empty and no goal was found, return the number of nodes explored and an empty path            