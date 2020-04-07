class Solution_1:
"""
Runtime: 224 ms, faster than 19.52% of Python3 online submissions for Course Schedule.
Memory Usage: 16 MB, less than 51.02% of Python3 online submissions for Course Schedule.

https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation

dfs
拓扑排序
"""
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
    
    def dfs(self, graph, visited, i):
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbours, mark it as done visited
        visited[i] = 1
        return True
        
        
class Solution_2:
"""
Runtime: 424 ms, faster than 16.96% of Python3 online submissions for Course Schedule.
Memory Usage: 15.1 MB, less than 65.31% of Python3 online submissions for Course Schedule.

https://blog.csdn.net/lym940928/article/details/89883416

bfs
"""
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 首先我们要重新构建有向图,因为题中是用list of edges表示,不利于解题;
        # 我们要将其转换为adjacency matrices.
        graph = self.build_graph(numCourses, prerequisites)
        # 计算入度.
        indegree = self.calculate_indegree(graph)
        
        # 这里的思想是循环numCourses次后就会得到答案
        # 其实并不是一定需要这么多次
        # 只需要检查入度为0的点就行，见solution3
        for _ in range(numCourses):
            k = 0 
            while k < numCourses:
                if indegree[k] == 0: #找到入度为0的点
                    break
                k += 1
            if k == numCourses:
                return False
            #由于indegree[k]=0,所以这里减1将其变为-1，相当于在graph中删掉这个点.
            indegree[k] -= 1 
            for item in graph[k]:
                indegree[item] -= 1
        return True
        
    def build_graph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            # 构建有向图，其中第二个指向第一个.
            graph[prerequisites[i][1]].append(prerequisites[i][0])
        return graph
    
    def calculate_indegree(self, graph):
        indegree = [0] * len(graph)
        for sublst in graph:
            for item in sublst:
                indegree[item] += 1
        return indegree
        
class Solution_3:
"""
Runtime: 232 ms, faster than 19.34% of Python3 online submissions for Course Schedule.
Memory Usage: 15.2 MB, less than 65.31% of Python3 online submissions for Course Schedule.

bfs,相较于solution2更好地使用了拓扑排序.

记这个!

"""
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.build_graph(numCourses, prerequisites)
        indegree = self.calculate_indegree(graph)
        
        queue = [] #维护一个队列，队列中是当前入度为0的点.
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        count = 0
        # 只需要检查入度为0的点.
        # 这才是拓扑排序的定义.
        while queue: 
            idx = queue.pop(0)
            k = 0
            indegree[idx] -= 1
            for item in graph[idx]:
                indegree[item] -= 1
                if indegree[item] == 0:
                    queue.append(item)
            count += 1
        # 判断是否经过了所有点.
        return True if count == numCourses else False
        
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