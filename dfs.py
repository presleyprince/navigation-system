# For the dfs search algorithm, make it a child of search_algorithm.py the SearchAlgorithm class
# the class has file reading functionality, formatting the node and edge data to be usable, and will eventually have
# the output functionality, it also has abstract methods that will need to be implemented here, being search and run_algorithm.
# - Jake
from search_algorithm import SearchAlgorithm

# get the variables and functions from SearchAlogrithm
class DepthFirstSearch(SearchAlgorithm):
    
    # innit means it will automatically run when DFS(Pathfinder-test.txt) is ran
    def __init__(self, filename):

        #need to run the parent class to setup first
        super().__init__() # creates self.Nodes, self.Edges, self.Origin, self.Goal

        self.read_file(filename) #read the file and fill in the variables needed

    def search(self, node):
        
        #dfs uses a stack method
        stack = []

        
        visited = [] #create a list of already visited notes so they get visited twice

        came_from = {} # helps to remeber how each node was reached, if it says eg [4] = 5 then we got to node 5 from node 4

        node_count = 0 # count the amount of nodes looked at

        stack.append(self.Origin) # put the starting node to the stack (self.Origin comes from the parent class)

        while stack: #loop until stack is empty

            current_node = stack.pop() #take the top node off the stack, pop() removes the last item in the list

            if current_node in visited: #if already visited the node skip it
                continue
            
            visited.append(current_node) # mark the ndoe as been visited

            node_count += 1 # +1 to the node counter

            if current_node in self.Goal: #check if the current node is on the destinations (self.Goal is a list of all destinations)

                path = [] # once at the destination find the path that was taking to reach

                node = current_node # start at the destination node

                while node in came_from: # going backwards till reaching the start

                    path.append(node) # add that node to the path
                    node = came_from[node] # go to the previous node

                path.append(self.Origin) #add the starting node to the path

                path.reverse() # reverse the path to go from the start to the goal since it's at the goal now to the start

                return node_count, path # return the number of nodes and the path
#started dfs need to fix up - presley