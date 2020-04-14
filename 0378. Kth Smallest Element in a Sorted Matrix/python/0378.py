class Solution_1:
"""
Runtime: 232 ms, faster than 34.99% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19.7 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

heap
"""
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [(row[0], i, 0) for i, row in enumerate(matrix)]
        heapq.heapify(heap)
        ret = 0
        for _ in range(k):
            ret, i, j = heapq.heappop(heap)
            if j+1 < len(matrix[0]):
                heapq.heappush(heap, (matrix[i][j+1], i, j+1))
        return ret
        
class Solution_2:
"""
Runtime: 180 ms, faster than 79.76% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19.7 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.

https://www.cnblogs.com/grandyang/p/5727892.html


这个好记!
"""
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = (l+r) // 2
            count = self.search_less_equal(matrix, mid)
            if count < k:
                l = mid +1
            else:
                r = mid
        return l
            
    def search_less_equal(self, matrix, target):
        i, j = len(matrix)-1, 0
        res = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= target:
                res += i+1 #注意这里是i+1,因为当前列的当前位置的上面所有的数字都小于目标值.
                j += 1
            else:
                i -= 1
        return res 