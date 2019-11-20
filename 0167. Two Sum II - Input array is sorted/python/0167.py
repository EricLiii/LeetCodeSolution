class Solution_1:
"""
Author: Zefeng

Runtime: 76 ms, faster than 64.14% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.3 MB, less than 5.83% of Python3 online submissions for Two Sum II - Input array is sorted.
"""
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dic:
                return [dic[target-numbers[i]], i+1]
            else:
                dic[numbers[i]] = i + 1
                
class Solution_2:
"""
Runtime: 76 ms, faster than 64.14% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.3 MB, less than 5.83% of Python3 online submissions for Two Sum II - Input array is sorted.
"""
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1      
                
class Solution_3:
"""
Runtime: 104 ms, faster than 13.56% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 14.4 MB, less than 5.83% of Python3 online submissions for Two Sum II - Input array is sorted.
"""
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1