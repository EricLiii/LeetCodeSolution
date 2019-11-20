class Solution_1:
"""
Runtime: 44 ms, faster than 80.77% of Python3 online submissions for Clone Graph.
Memory Usage: 14.6 MB, less than 7.41% of Python3 online submissions for Clone Graph.

递归

思路：
使用一个字典来映射source和copy。
遍历node的neighbor，检查是否已经创建了neighbor*(neighbor*的邻居是否已找全先不管).
如果已经创建，则将neighbor*加入node*的邻居中;
如果未创建，创建neighbor*，同时将neighbor*加入node*的邻居中.dfs(neighbor*).

以题中的1,2,3,4为例。以下是步骤：
(1) 1[2,4]: 1*[]

(2) 1[2,4]: 1*[2*]
    2[1,3]: 2*[]

(3) 1[2,4]: 1*[2*]
    2[1,3]: 2*[1*]

(4) 1[2,4]: 1*[2*]
    2[1,3]: 2*[1*,3*]
    3[2,4]: 3*[]

(5) 1[2,4]: 1*[2*]
    2[1,3]: 2*[1*,3*]
    3[2,4]: 3*[2*]

(6) 1[2,4]: 1*[2*]
    2[1,3]: 2*[1*,3*]
    3[2,4]: 3*[2*,4*]    
    4[1,3]: 4*[]

(7) 1[2,4]: 1*[2*]
    2[1,3]: 2*[1*,3*]
    3[2,4]: 3*[2*,4*]    
    4[1,3]: 4*[1*]

(8) 1[2,4]: 1*[2*]
    2[1,3]: 2*[1*,3*]
    3[2,4]: 3*[2*,4*]    
    4[1,3]: 4*[1*,3*]

(9) 1[2,4]: 1*[2*,4*]
    2[1,3]: 2*[1*,3*]
    3[2,4]: 3*[2*,4*]    
    4[1,3]: 4*[1*,3*]
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
                #注意:如果已经有了neighbor，则不需要再调用dfs.
                #这保证了可以退出函数,而不是陷入dead loop.
                self.visited[node].neighbors.append(self.visited[neighbor])