from abc import ABC, abstractmethod
import math

class SearchAlgorithm(ABC):
    def __init__(self):
        self.Nodes = []
        self.Edges = []
        self.Origin = None
        self.Goal = []
    
    def node_id(self, node):
        '''This function returns the node id from a given node entry.'''
        return node.split(":")[0]
        
    def format_edge(self, edge):
        '''This function returns the current_node, next_node and cost from a given edge entry.'''
        left, right = edge.split(":")
        cost = int(right.strip())

        current_node, next_node = left.strip("()").split(",")
        return current_node.strip(), next_node.strip(), cost
        
    def read_file(self, filename):
        '''This function reads the given file and fills the variables: Nodes, Edges, Origin and Goal.'''
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
                
                if any(not getattr(self, var) for var in headers.values()):
                    raise ValueError("Missing required data in the file.")

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
    
    def create_output(self, filename, method, number_of_nodes, path):
        # def create_output(self, filename, method, number_of_nodes, path, current_mem, peak_mem, time_elapsed, cpu_percent):
        '''This functions creates an output based on the given method, number_of_nodes and path.'''
        goal = path[-1] if path else "None" # This will get the last node in the path as the goal, if the path is empty, it will indicate that as well.
        path_output = ", ".join(path) if path else "No path found" # This will create a string representation of the path taken.

        print(f"{filename} {method}")
        print(f"{goal} {number_of_nodes}")
        print(f"[{path_output}]")
        # print(f"\nResources used\nTime: {time_elapsed:.4f} seconds, Memory: Current = {current_mem / 1024:.2f} KB, Peak = {peak_mem / 1024:.2f} KB, CPU: {cpu_percent:.2f}%")

    def reconstruct_path(self, goal_node): # This is a helper function to reconstruct the path from the origin to the goal node using the parent links
        '''This path reconstructs the path from the origin to the goal node using the parent links.'''
        path = []
        current = goal_node

        while current is not None: # Reconstruct the path by following the parent links from the goal node back to the origin node
            path.append(current)
            current = self.parent.get(current)

        path.reverse()  # Reverse the path to get the correct order from start to goal
        return path
    
    def build_node_positions(self):
        '''This function builds a dictionary of node positions for heuristic calculations.'''
        positions = {}
        for node in self.Nodes:
            node_id, coordinates = node.split(":")
            x, y = coordinates.strip().strip("()").split(",")
            positions[node_id.strip()] = (float(x.strip()), float(y.strip()))
        return positions
    
    def heuristic(self, node_id):
        '''This function calculates the heuristic value for a given node based on the nearest goal distance.'''
        # GBFS: f(n) = h(n), use nearest goal distance
        x1, y1 = self.node_positions[node_id]
        best = float('inf')
        for goal_id in self.Goal:
            if goal_id not in self.node_positions:
                continue
            x2, y2 = self.node_positions[goal_id]
            h = math.hypot(x2 - x1, y2 - y1)  # Euclidean distance as heuristic
            if h < best:
                best = h
        return best
    
    @abstractmethod
    def search(self, node):
        '''This is a function to run a singular search.'''
        pass

    @abstractmethod
    def run_algorithm(self):
        '''This is a function to run the entire algorithm, repeating searches until a path is found.'''
        pass