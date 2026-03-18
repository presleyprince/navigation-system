# Jake, Kyle
from search_algorithm import SearchAlgorithm

class BreadthFirstSearch(SearchAlgorithm):
        def __init__(self):
            # Initializing the variable, from parent and needed bfs specific variables
            super().__init__()
            self.explored_nodes = []

        # TODO: Implement breadth-first search algorithm here
        def search(self, node):
            # Origin is 2, check if 2 is goal, check what connects to 2, list those, run those after, don't check backwards
            node_id = self.node_id(node)
            if node_id == self.Goal:
                return node

            for edge in self.Edges:
                current_node, next_node, cost = self.format_edge(edge)
                if current_node == node_id:
                    # Add next_node to the queue for further exploration if not already explored
                    if next_node not in self.explored_nodes:
                        pass
                    # Also total cost should be tracked and updated here for that path
                    pass

        def run_algorithm(self):
            # Run until reaches the goal
            explored_nodes = []
            next_nodes = []

            # if self.breadth_first_search(self.Origin) in self.Goal: # Doesn't currently work
            #     print("Goal reached!")
            #     return

            # while True:
            #     pass

