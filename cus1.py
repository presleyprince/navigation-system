from search_algorithm import SearchAlgorithm
import heapq

class BeamSearch(SearchAlgorithm):
    def __init__(self, beam_width=2): 
        super().__init__()
        self.beam_width = beam_width
        self.queue = []
        self.parent = {}
        self.visited = set()
        self.explored_nodes = []

    def search(self, current_level):
        next_level = []

        for node in current_level:
            for edge in self.Edges:
                if ":" not in edge:
                    continue

                current_node, next_node, cost = self.format_edge(edge)

                if current_node != node:
                    continue

                if next_node in self.visited:
                    continue

                if next_node not in self.parent:
                    self.parent[next_node] = node

                h = self.heuristic(next_node)
                next_level.append((h, next_node))

        # Sort by heuristic (smallest first)
        next_level.sort(key=lambda x: (x[0], x[1]))

        # Keep only top k nodes (beam width)
        return [node for _, node in next_level[:self.beam_width]]

    def run_algorithm(self):
        if self.Origin is None:
            return (0, [])

        self.node_positions = self.build_node_positions()

        current_level = [self.Origin]
        self.parent = {self.Origin: None}
        self.visited = set([self.Origin])
        self.explored_nodes = []

        while current_level:
            next_level = []

            for node in current_level:
                if node in self.visited:
                    continue

                self.visited.add(node)
                self.explored_nodes.append(node)

                if node in self.Goal:
                    path = self.reconstruct_path(node)
                    return (len(self.explored_nodes), path)

            # Expand current level
            next_level = self.search(current_level)

            # Mark next level as visited
            for node in next_level:
                self.visited.add(node)

            current_level = next_level

        return (len(self.explored_nodes), [])
