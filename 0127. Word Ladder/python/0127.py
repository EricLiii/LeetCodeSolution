class Solution_1:
"""
Runtime: 464 ms, faster than 41.20% of Python3 online submissions for Word Ladder.
Memory Usage: 14.8 MB, less than 48.28% of Python3 online submissions for Word Ladder.

https://leetcode.com/problems/word-ladder/discuss/157376/Python-(BFS)-tm


https://blog.csdn.net/fuxuemingzhu/article/details/82903681 这个讲的清楚!!!
根据这个link,这个题是走迷宫问题的变,也就是说,我们每次变化有26个方向,如果变化之后的位置在wordList中,我们认为这个走法是合规的,最后问能不能走到endWord.
这里有一点需要注意，我们用一个visited来保存已经走过的路径.假设我们现在从一个位置a出发,有两条路径可选： a->b,a->c.
我们将b,c都标为visited.可是如果我们不从c走而是从b走，假如之后走到了c,但是我们已经将c标为visited,直接返回,这样不就出错了吗?
其实是这样的，如果a->b->...->c->...这条路能到达终点，那么a->c->...也能到达终点.也就是说a->b不是最短路径。
这也就是为什么我们可以将b,c均标为visited而不会出错.

一般搜索最短路径都是用bfs,搜索全部路径用dfs.
"""
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #防止time exceed
        #这行 if new_word in wordList ，如果wordList是list，时间复杂度为O(n);如果wordList是set，时间复杂度为O(1).
        wordList = set(wordList) 
        q = collections.deque([(beginWord, 1)])
        visted = set()
        alpha = string.ascii_lowercase  #'abcd...z'  也有不需要遍历26个字母的方法，以后有时间细看.
        while q:
            word, length = q.popleft()
            #如何保证最短？因为是bfs，所以只要word == endWord，那么就是最短.
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in wordList and new_word not in visted:
                        q.append((new_word, length + 1))
                        visted.add(new_word)
        return 0