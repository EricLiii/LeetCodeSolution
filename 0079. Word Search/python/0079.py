class Solution_1:
"""
Runtime: 404 ms, faster than 9.91% of Python3 online submissions for Word Search.
Memory Usage: 15.3 MB, less than 14.92% of Python3 online submissions for Word Search.

Idea:
每当发现word的第一个元素，就在上下左右进行寻找。
"""
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                #这里很重要，只有当dfs返回True的时候才返回True。这是因为有时可能从当前元素出发找不到word，
                #这时就要跳到board的下一个元素。如果return self.dfs(board, i, j, word),可能就直接退出算法了。
                if self.dfs(board, i, j, word):
                    return True
        #如果遍历所有元素都没找到，就返回False.
        return False
        
    def dfs(self, board, i, j, word):
        #如果word中的元素都被找到了，就返回True.
        if not word:
            return True
        #防止越界.
        if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1:
            return False
        if board[i][j] == word[0]:
            #这里要改变board[i][j]的值，防止下一个元素在上下左右判断时重复判断board[i][j]
            #由于board中均为字符，所以我将其设为int，int!=char.
            tmp = board[i][j]
            board[i][j] = 0 
            #这里要注意先用res来保存返回值，然后恢复board[i][j]，最后再返回res。
            #否则如果直接return四个dfs的或，可能在深层的dfs就返回False了，这样就没有恢复现场。
            res =  self.dfs(board, i, j+1, word[1:]) or \
                   self.dfs(board, i, j-1, word[1:]) or \
                   self.dfs(board, i+1, j, word[1:]) or \
                   self.dfs(board, i-1, j, word[1:]) 
            #恢复现场。
            board[i][j] = tmp
            return res
        else:
            return False
            
class Solution_2:
"""
Runtime: 284 ms, faster than 52.56% of Python3 online submissions for Word Search.
Memory Usage: 15.5 MB, less than 14.70% of Python3 online submissions for Word Search.

Idea: 
没有一次性迭代四次dfs，而是逐个迭代，如果True就及时退出，这样就减少了运行时间。
"""
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        def spread(i, j, w):
            if not w:
                return True
            original, board[i][j] = board[i][j], '-'
            spreaded = False
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if (0 <= x< R and 0 <= y < C and w[0] == board[x][y] and spread(x, y, w[1:])):
                    #spreaded = True
                    #break  
                    return True #及时退出
            board[i][j] = original
            return spreaded

        for i in range(R):
            for j in range(C):
                if board[i][j] == word[0] and spread(i, j, word[1:]):
                    return True
        return False
        
class Solution_3:
"""
Zefeng
自己写的，好像比solution_1简洁，但是没有2简洁.

Runtime: 380 ms, faster than 44.34% of Python3 online submissions for Word Search.
Memory Usage: 15.2 MB, less than 17.02% of Python3 online submissions for Word Search.
"""
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, [(i,j)], word):
                    return True
        return False
        
    def helper(self, board, stack, word):
        if not word:
            return True
        while stack:
            item = stack.pop()
            i, j = item[0], item[1]
            # 注意上界和下界都要比较
            if 0 <= i <len(board) and 0 <= j < len(board[0]):
                if board[i][j] == word[0]:
                    temp = word[0]
                    board[i][j] = '-'
                    new = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                    if self.helper(board, new, word[1:]):
                        return True
                    else:
                        board[i][j] = temp
        return False