class Solution:
"""
Runtime: 484 ms, faster than 49.59% of Python3 online submissions for Word Ladder II.
Memory Usage: 16.8 MB, less than 71.96% of Python3 online submissions for Word Ladder II.

https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
"""
    def findLadders(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            print(layer)
            """
            defaultdict(<class 'list'>, {'hot': [['hit', 'hot']]})
            defaultdict(<class 'list'>, {'dot': [['hit', 'hot', 'dot']], 'lot': [['hit', 'hot', 'lot']]})
            defaultdict(<class 'list'>, {'dog': [['hit', 'hot', 'dot', 'dog']], 'log': [['hit', 'hot', 'lot', 'log']]})
            defaultdict(<class 'list'>, {'cog': [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]})
            """
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res += [k for k in layer[w]]
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww] += [x+[neww] for x in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res