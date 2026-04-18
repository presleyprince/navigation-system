from search_algorithm import SearchAlgorithm

class BeamSearch(SearchAlgorithm):
    def __init__(self, beam_width=2):
        super().__init__()
        self.beam_width = beam_width
        self.parent = {}
        self.visited = set()
        self.explored_nodes = []

    def search(self, node):
        neighbors = []

        for edge in self.Edges:
            if ":" not in edge:
                continue

            src, dst, cost = self.format_edge(edge)

            if cost < 0:
                raise ValueError("Edge costs must be non-negative")

            if src == node and dst not in self.visited:
                neighbors.append(dst)

        return neighbors

    def run_algorithm(self):
        if self.Origin is None:
            return (0, [])

        self.node_positions = self.build_node_positions()

        current_level = [self.Origin]
        self.parent = {self.Origin: None}
        self.visited = set()
        self.explored_nodes = []

        while current_level:
            next_candidates = []

            for node in current_level:
                if node in self.visited:
                    continue

                self.visited.add(node)
                self.explored_nodes.append(node)

                if node in self.Goal:
                    path = self.reconstruct_path(node)
                    return (len(self.explored_nodes), path)

                neighbors = self.search(node)

                for n in neighbors:
                    if n not in self.parent:
                        self.parent[n] = node

                    h = self.heuristic(n)
                    next_candidates.append((h, n))

            # Sort by heuristic (then node id for tie-breaking)
            next_candidates.sort(key=lambda x: (x[0], x[1]))

            # Beam width pruning
            current_level = [node for _, node in next_candidates[:self.beam_width]]

        return (len(self.explored_nodes), [])
