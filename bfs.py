# Jake, Kyle
from search_algorithm import SearchAlgorithm

class BreadthFirstSearch(SearchAlgorithm):
        def __init__(self):
            # Initializing the variable, from parent and needed bfs specific variables
            super().__init__()
            self.explored_nodes = [] # Temp, change if needed or use if needed
            # I recommend probably using a dictionary to track the nodes gone too, we need the parent id of which edge was traveled to get to the node
            # the dictionary can also hold the information of where the node is and which edge it used to get there, with the parent id being the previous node
            # this is needed as we need to output the path taken, which requires us to know which nodes had been traveled to get there.

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
            # Run until reaches the goal, uses search do to so
            pass
            
            # Needs to output 2 things, the number of nodes traveled, and the path taken as a list, being (number_of_nodes_traveled, path)

