class Solution_1:
"""
Runtime: 44 ms, faster than 49.48% of Python3 online submissions for Subsets.
Memory Usage: 13.9 MB, less than 5.27% of Python3 online submissions for Subsets.

Idea:
DFS recursively 
"""
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
            
class Solution_2:
"""
Runtime: 40 ms, faster than 79.79% of Python3 online submissions for Subsets.
Memory Usage: 14.1 MB, less than 5.27% of Python3 online submissions for Subsets.

Idea:
Iteratively
"""
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res
        
class Solution_3:
"""
Runtime: 36 ms, faster than 94.57% of Python3 online submissions for Subsets.
Memory Usage: 14 MB, less than 5.27% of Python3 online submissions for Subsets.

Idea:
Bit Manipulation.
1. <<: 是python的左移操作。例如2<<2=8,就是说先把2转换成二进制010，然后左移两位就是1000，即十进制的8.
2. &:  是按位与操作。例如3&2=2,就是先把3转换成011，2转换成010.然后每一位进行与操作，结果为010.
3. 这个方法可以参考https://www.geeksforgeeks.org/power-set/。
    具体就是先求出子集的个数，即pow(2, len(nums))。以[1,2,3]为例，子集个数为8.
    000 -> []
    001 -> [1]
    010 -> [2]
    011 -> [1,2]
    100 -> [3]
    101 -> [1,3]
    110 -> [2,3]
    111 -> [1,2,3]
"""
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1<<len(nums)):   # 1<<3 = 8, 即子集个数为8
            tmp = []
            for j in range(len(nums)):  # j取值为0, 1, 2
                if i & 1 << j:   
                    # 十进制1即二进制001，每次左移j位，与i进行按位与操作。
                    # 其实就是判断i转换成二进制后哪些位是1，哪些是0.
                    # 是1的话就append对应数字。
                    tmp.append(nums[j])
            res.append(tmp)
        return res