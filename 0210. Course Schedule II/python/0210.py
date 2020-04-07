class Solution_1:
"""
Zefeng

Runtime: 196 ms, faster than 10.35% of Python3 online submissions for Course Schedule II.
Memory Usage: 15 MB, less than 64.29% of Python3 online submissions for Course Schedule II.

bfs

跟0207类似
"""
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = self.build_graph(numCourses, prerequisites)
        indegree = self.calculate_indegree(graph)
        
        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        path = []
        count = 0
        while queue:
            idx = queue.pop(0)
            k = 0
            indegree[idx] -= 1
            for item in graph[idx]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
            path.append(idx)
            count += 1
        return path if count == numCourses else []
        
    def build_graph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        return graph
    
    def calculate_indegree(self, graph):
        indegree = [0] * len(graph)
        for sublst in graph:
            for item in sublst:
                indegree[item] += 1
        return indegree
        
        
class Solution_2:
"""
TODO: 用dfs做!

"""
