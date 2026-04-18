# Jake, Kyle
# deque is a double ended queue, which allows us to efficiently add and remove elements from both ends. This is useful for implementing the breadth-first search algorithm, as we can easily add new nodes to the end of the queue and remove nodes from the front of the queue for exploration.
from collections import deque
from search_algorithm import SearchAlgorithm

class BreadthFirstSearch(SearchAlgorithm):
        def __init__(self):
            # Initializing the variables, from parent and needed bfs specific variables
            super().__init__()
            self.queue = deque()
            self.visited = set()
            self.parent = {}
            self.explored_count = 0

        def search(self, node):
            # Origin is 2, check if 2 is goal, check what connects to 2, list those, run those after, don't check backwards
            node_id = self.node_id(node)
            if node_id in self.Goal:
                return node

            neighbors = []
            for edge in self.Edges:
                if ":" not in edge:
                    continue
                current_node, next_node, _ = self.format_edge(edge)
                if current_node == node_id and next_node not in self.visited:
                    neighbors.append(next_node)

            neighbors.sort()  # Sort neighbors to ensure consistent order of exploration

            for next_node in neighbors:
                # Add next_node to the queue for further exploration if not already explored
                self.visited.add(next_node)
                self.parent[next_node] = node_id  # Track the parent of the next_node for path reconstruction
                self.queue.append(next_node)

        def run_algorithm(self):
            if self.Origin is None:
                return (0, [])  # No origin node defined, cannot run the algorithm
            
            self.queue = deque([self.Origin])  # Start with the origin node in the queue
            self.visited = {self.Origin}  # Mark the origin node as visited
            self.parent = {self.Origin: None}  # The origin node has no parent
            self.explored_nodes = []  # List to keep track of explored nodes

            while self.queue:
                current_node = self.queue.popleft()  # Get the next node to explore from the front of the queue
                self.explored_nodes.append(current_node)  # Add the current node to the list of explored nodes
                
                if current_node in self.Goal:
                    path = self.reconstruct_path(current_node)  # Reconstruct the path from the origin to the goal
                    return (len(self.explored_nodes), path)  # Return the number of nodes explored and the path taken
                
                self.search(current_node)  # Explore the current node and add its neighbors to the queue

            return (len(self.explored_nodes), [])  # If the queue is empty and no goal was found, return the number of nodes explored and an empty path            

