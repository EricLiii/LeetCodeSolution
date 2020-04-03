class Solution:
"""
Runtime: 108 ms, faster than 78.40% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.3 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.

https://leetcode.com/problems/top-k-frequent-elements/discuss/81697/Python-O(n)-solution-without-sort-without-heap-without-quickselect
code在comment里.
"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z,v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        
        arr = []
        
        for x in range(len(nums), 0, -1):
            if x in frq:
		#这里直接相加，不要像link里用for，会更快.
		#同时用for应该就不是O(n)了。
                arr += frq[x] 
        return arr[:k]
