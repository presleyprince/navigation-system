# For the dfs search algorithm, make it a child of search_algorithm.py the SearchAlgorithm class
# the class has file reading functionality, formatting the node and edge data to be usable, and will eventually have
# the output functionality, it also has abstract methods that will need to be implemented here, being search and run_algorithm.
# - Jake
from search_algorithm import SearchAlgorithm

# get the variables and functions from SearchAlogrithm
class DepthFirstSearch(SearchAlgorithm):
    
    # innit means it will automatically run when DFS(Pathfinder-test.txt) is ran
    def __init__(self):
        #need to run the parent class to setup first
        super().__init__() # creates self.Nodes, self.Edges, self.Origin, self.Goal
        self.stack = [] # nodes to visit, taking from top 
        self.visited = [] # list of nodes already been to 
        self.parent = {} # how each node was reached
        self.explored_nodes = [] # keep count of every node looked at already for final result
   

    def search(self, node): # removed unused 'node' parameter, start node comes from self.Origin

        node_id = self.node_id(node) # getting the id of the current node to use for parent class 
        
        if node_id in self.Goal: # check if it's already at the goal
            return node

        for edge in self.Edges: #finding all neighbours from the current node
            if ":" not in edge: # skipping blanks or it will crash
                continue
            current_node, next_node, cost = self.format_edge(edge) # take out src and dest from the edge strings through the parent class helper
            if current_node == node_id and next_node not in self.visited:
                if next_node not in self.parent: # writing down only how it reached here from the first time
                    self.parent[next_node] = node_id
                self.visited.append(next_node)
                self.stack.append(next_node) # add the neighbour to the stack to visit

    def run_algorithm(self):
        if self.Origin is None:
            return (0, [])  # no starting node to run
        
        self.stack = [self.Origin]           # starting with the origin node on the stack
        self.visited = [self.Origin]         # marking the origin as visited so don't go back to it again
        self.parent = {self.Origin: None} # the origin doesn't have a parent so it is the start
        self.explored_nodes = []             # reset the explored nodes list
        
        while self.stack:
            current_node = self.stack.pop()          # taking from the top of the stack
            self.explored_nodes.append(current_node) # writing this node was visited

            if current_node in self.Goal:            # checking if the goal is reached
                path = self.reconstruct_path(current_node) # tracing back to find the path
                return (len(self.explored_nodes), path)

            self.search(current_node) # checking the neighbouring nodes of the current node
        
        return (len(self.explored_nodes), []) # stack is empty, no path will be found


if __name__ == "__main__":
    dfs = DepthFirstSearch()
    dfs.read_file("PathFinder-test1.txt")
    number_of_nodes, path = dfs.run_algorithm()
    print(number_of_nodes, path)
