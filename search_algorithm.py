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
        headers = {
        "Nodes:": "Nodes",
        "Edges:": "Edges",
        "Origin:": "Origin",
        "Destinations:": "Goal",
        }

        # Reading the file and filling the variables
        try:
            with open(filename, "r") as file:
                # Reading the entire file and spliting it into lines
                data = file.read()
                data = data.splitlines()
                dataType = None

                for line in data:
                    # Checking what the current dataType is
                    if line in headers:
                        dataType = headers[line]
                        continue
                        
                    # Raises an error if the dataType is not recognized, this means the file is not in the correct format
                    if dataType is None:
                        raise ValueError("Invalid file format.")

                    # FIlling the correct variable based on the current dataType
                    match dataType:
                        case "Nodes":
                            self.Nodes.append(line)
                        case "Edges":
                            self.Edges.append(line)
                        case "Origin":
                            self.Origin = line
                        case "Goal":
                            # The goal is split into a list as there can be multiple goals
                            self.Goal.extend(part.strip() for part in line.split(";") if part.strip())
                
                return True
        # Handling exceptions
        except Exception as e:
            # Handles the case where the file is not found
            if isinstance(e, FileNotFoundError):
                print(f"Error: File '{filename}' not found.")
            # Handles the other error cases
            else:
                print(f"An error occurred while reading the file: {e}")
            return False
    
    def create_output(self, method, number_of_nodes, path):
        goal = path[-1] if path else "None" # This will get the last node in the path as the goal, if the path is empty, it will indicate that as well.
        path_output = " -> ".join(path) if path else "No path found" # This will create a string representation of the path taken, with nodes separated by " -> ". If no path is found, it will indicate that as well.

        print(f"Method: {method}")
        print(f"Goal: {goal}, Number of Nodes: {number_of_nodes}")
        print(f"Path: {path_output}")

    def reconstruct_path(self, goal_node): # This is a helper function to reconstruct the path from the origin to the goal node using the parent links
             path = []
             current = goal_node

             while current is not None: # Reconstruct the path by following the parent links from the goal node back to the origin node
                 path.append(current)
                 current = self.parent.get(current)

             path.reverse()  # Reverse the path to get the correct order from start to goal
             return path
    
    @abstractmethod
    def search(self):
        pass

    @abstractmethod
    def run_algorithm(self):
        pass