class Solution:
"""
Runtime: 240 ms, faster than 97.12% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 17.1 MB, less than 75.00% of Python3 online submissions for Minimum Height Trees.

https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
"""
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0] 
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves
