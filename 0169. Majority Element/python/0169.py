class Solution_1:
"""
Author: Zefeng

Runtime: 200 ms, faster than 52.04% of Python3 online submissions for Majority Element.
Memory Usage: 15.2 MB, less than 5.53% of Python3 online submissions for Majority Element.
"""
    def majorityElement(self, nums: List[int]) -> int:
        c = len(nums)//2
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        for k, v in dic.items():  # 记住获取dict的键值对的方法,千万别忘了dict要先调用items().
            if v > c:
                return k
                
class Solution_2:
"""
这个算法很巧妙，值得学习！

Runtime: 188 ms, faster than 92.59% of Python3 online submissions for Majority Element.
Memory Usage: 15.2 MB, less than 5.53% of Python3 online submissions for Majority Element.

Idea:
Boyer-Moore Majority Vote Algorithm.

Link: https://www.cnblogs.com/javanerd/p/6262249.html

思路其实就是"兑子"。

原题是：假设有一群投票的人，每个人都会投票个某个候选人。为了选择最终赢的选取的候选人，
    可以采用这样的选举方式：每个投票人找到其他的投票人，并且这个投票人支持的候选不同于自己的支持的候选人，
    PK过后，这一对投票人同时出局。经过全部的PK之后，那么还没有出局的投票人支持的候选人，
    就有可能是最终的选举胜利者（获得半数以上的选票）。最后，选举主席，需要检查这位可能赢得选举的候选人的票数，来确认他是否赢得了选举。
    
而在本题中，由于已经声明maj一定存在，所以最后留下的maj一定就是majority element.

"""
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        c = 1
        for i in range(1, len(nums)):
            if c == 0:
                c +=1
                maj = nums[i]
            elif maj == nums[i]:
                c += 1
            else:
                c -= 1
        return maj