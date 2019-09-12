class Solution_1:
"""
Runtime: 464 ms, faster than 41.20% of Python3 online submissions for Word Ladder.
Memory Usage: 14.8 MB, less than 48.28% of Python3 online submissions for Word Ladder.

https://leetcode.com/problems/word-ladder/discuss/157376/Python-(BFS)-tm

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
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in wordList and new_word not in visted:
                        q.append((new_word, length + 1))
                        visted.add(new_word)
        return 0