class Solution_1:
"""
Zefeng

Runtime: 40 ms, faster than 94.68% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14.1 MB, less than 5.72% of Python3 online submissions for Intersection of Two Arrays II.
"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for i in range(len(nums1)):
            if nums1[i] in dic:
                dic[nums1[i]] += 1
            else:
                dic[nums1[i]] = 1
        # 改进, 以后要这样写才简洁!
        #for i in range(len(nums1)):
        #    dic[nums1[i]] = dic.get(nums1[i],0) + 1
        
        arr = []
        for j in range(len(nums2)):
            if nums2[j] in dic and dic[nums2[j]] > 0:
                arr.append(nums2[j])
                dic[nums2[j]] -= 1
        return arr
        
        
#TODO: 后面还有3个场景，以后做!