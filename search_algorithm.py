from abc import ABC, abstractmethod

class SearchAlgorithm(ABC):
    def __init__(self):
        self.Nodes = []
        self.Edges = []
        self.Origin = None
        self.Goal = []
    
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
    
    # TODO: Create output in filename method, goal number_of_nodes, and path
    def create_output(self):
        pass

    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def run_algorithm(self):
        pass