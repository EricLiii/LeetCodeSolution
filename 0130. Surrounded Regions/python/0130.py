class Solution:
"""
Runtime: 152 ms, faster than 94.68% of Python3 online submissions for Surrounded Regions.
Memory Usage: 14.8 MB, less than 53.33% of Python3 online submissions for Surrounded Regions.

Link: https://leetcode.com/problems/surrounded-regions/discuss/41630/9-lines-Python-148-ms
"""
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not any(board): return

        m, n = len(board), len(board[0])
        #range(m+n)换成range(max(m,n))更好。
        #因为这里range(m+n)不是为了让k一定要取到m+n，而是为了保证k一定能取到m,n中的最大值
        #(因为m可能不等于n)。
        #这样save才能访问到board所有边界上的值.
        #之前就是因为range(m+n)的写法而让我感到有些迷惑.
        save = [item for k in range(m+n) for item in ((0, k), (m-1, k), (k, 0), (k, n-1))]

        #找出所有在边界上的O        
        while save:
            i, j = save.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                save += (i, j-1), (i, j+1), (i-1, j), (i+1, j)  #将这个O的上下左右元素放入save.
 
        board[:] = [["O" if c == "S" else "X" for c in row] for row in board] #将所有S换成O，其他的换成X.