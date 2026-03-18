# This file will be used to call the search algorithms!
import sys
from bfs import SearchAlgorithm
# from dfs import SearchAlgorithm

def main():
    # Checks the size of the system arguments
    if len(sys.argv) != 3:
        print("Usage: python program.py <filename> <method>")
        return
    
    # Gets the filename and method from the system arguments
    filename = sys.argv[1]
    method = sys.argv[2]

    # Calls the correct method based on the method argument
    try:
        # Calls the bfs method
        if method.lower().strip() == "bfs":
            search = SearchAlgorithm()
            search.read_file(filename)
            search.breadth_first_search()

        # Calls the dfs method
        elif method.lower().strip() == "dfs":
            print("DFS method is not implemented yet.")

        else:
            # Handles the case where the method is not valid
            raise ValueError("Invalid method.")

    # Handles any other exceptions that may occur
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()