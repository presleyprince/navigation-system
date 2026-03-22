# This file will be used to call the search algorithms!
import sys
from bfs import BreadthFirstSearch
# from dfs import DepthFirstSearch

# The algorithm Dictionary
ALGORITHMS = {
    "bfs": BreadthFirstSearch,
    # "dfs": DepthFirstSearch,
    }

def main():
    # Checks the size of the system arguments
    if len(sys.argv) != 3:
        print("Usage: python program.py <filename> <method>")
        return
    
    # Gets the filename and method from the system arguments
    filename = sys.argv[1]
    method = sys.argv[2]

    algorithm_cls = ALGORITHMS.get(method.lower().strip())
    if algorithm_cls is None:
        print(f"Error: Invalid method '{method}'. Valid methods are: {', '.join(ALGORITHMS.keys())}.")
        return
    
    search = algorithm_cls()
    if search.read_file(filename):
        return
    number_of_nodes, path = search.run_algorithm() # This will run the algorithm and return the number of nodes explored and the path taken
    search.create_output(method, number_of_nodes, path) # This will create the output based on the method, number of nodes explored and the path taken

if __name__ == "__main__":
    main()