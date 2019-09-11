class Solution_1:
"""
Runtime: 44 ms, faster than 80.77% of Python3 online submissions for Clone Graph.
Memory Usage: 14.6 MB, less than 7.41% of Python3 online submissions for Clone Graph.

有点乱，以后再仔细看看.
"""
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        self.visited = dict()
        node_copy = Node(node.val, [])
        self.visited[node] = node_copy
        self.dfs(node)
        return node_copy
    
    def dfs(self, node):
        for neighbor in node.neighbors:
            if neighbor not in self.visited:    # add the neighbor node to visited dict
                neighbor_copy = Node(neighbor.val, [])
                self.visited[neighbor] = neighbor_copy
                self.visited[node].neighbors.append(neighbor_copy)
                self.dfs(neighbor)
            else:   # use the neighbor node in the visited dict
                self.visited[node].neighbors.append(self.visited[neighbor])