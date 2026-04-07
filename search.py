# This file will be used to call the search algorithms!
import sys
import time
import tracemalloc
import psutil
from bfs import BreadthFirstSearch
from dfs import DepthFirstSearch
# from astar import AStarSearch # Named astar because 'as' conflicts with the reserved keyword 'as' in Python
from gbfs import GreedyBestFirstSearch
# from cus2 import DijkstraSearch

# The algorithm Dictionary
ALGORITHMS = {
    "bfs": BreadthFirstSearch,
    "dfs": DepthFirstSearch,
    # "as": AStarSearch,
    "gbfs": GreedyBestFirstSearch,
    # "cus2": DijkstraSearch,
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

    # Start resource monitoring and timing
    process  = psutil.Process() # Get the object for CPU monitoring
    process.cpu_percent(interval=0) # Initialize CPU monitoring
    tracemalloc.start() # Start monitoring memory usage
    time_start = time.time() # Start the timer

    
    if not search.read_file(filename):
        return
    number_of_nodes, path = search.run_algorithm() # This will run the algorithm and return the number of nodes explored and the path taken

    # Stop resource monitoring and timing
    time_elapsed = time.time() - time_start # Stop the timer and calculate elapsed time
    cpu_percent = process.cpu_percent(interval=0) # Get the CPU usage percentage
    current_mem, peak_mem = tracemalloc.get_traced_memory() # Get the current and peak memory usage
    tracemalloc.stop() # Stop monitoring memory usage

    search.create_output(method, number_of_nodes, path, current_mem, peak_mem, time_elapsed, cpu_percent) # This will create the output based on the method, number of nodes explored and the path taken

if __name__ == "__main__":
    main()