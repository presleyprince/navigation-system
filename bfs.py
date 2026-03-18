# Jake, Kyle
class BreadthFirstSearch:
        def __init__(self):
            # Initializing the variables holding the data from the file
            self.Nodes = []
            self.Edges = []
            self.Origin = None
            self.Goal = []
            self.explored_nodes = []

        def breadth_first_search(self, node):
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
                

        def node_id(self, node):
            return node.split(":")[0]
        
        def format_edge(self, edge):
            left, right = edge.split(":")
            cost = int(right.strip())

            current_node, next_node = left.strip("()").split(",")
            return current_node.strip(), next_node.strip(), cost
        
        def read_file(self, filename):
            # Reading the file and filling the variables
            try:
                with open(filename, "r") as file:
                    # Reading the entire file and spliting it into lines
                    data = file.read()
                    data = data.splitlines()

                    # Checking what the current dataType is
                    for line in data:
                        if line == "Nodes:":
                            dataType = "Nodes"
                            continue
                        elif line == "Edges:":
                            dataType = "Edges"
                            continue
                        elif line == "Origin:":
                            dataType = "Origin"
                            continue
                        elif line == "Destinations:":
                            dataType = "Goal"
                            continue
                        
                        # FIlling the correct variable based on the current dataType
                        match dataType:
                            case "Nodes":
                                self.Nodes.append(line)
                            case "Edges":
                                self.Edges.append(line)
                            case "Origin":
                                self.Origin = line
                            case "Goal":
                                self.Goal.extend(part.strip() for part in line.split(";") if part.strip())

            # Handling the case where the file is not found
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")
                return None

        def run_algorithm(self):
            # Run until reaches the goal
            explored_nodes = []
            next_nodes = []

            if self.breadth_first_search(self.Origin) in self.Goal: # Doesn't currently work
                print("Goal reached!")
                return

            while True:
                pass

        def create_output(self):
            pass

# TODO: Implement breadth-first search algorithm here
# TODO: Create output in filename method, goal number_of_nodes, and path