class Solution:
"""
Runtime: 68 ms, faster than 79.36% of Python3 online submissions for Contains Duplicate III.
Memory Usage: 15.8 MB, less than 33.33% of Python3 online submissions for Contains Duplicate III.

桶排序.

Link: https://leetcode.com/problems/contains-duplicate-iii/discuss/61731/O(n)-Python-using-buckets-with-explanation-10-lines.
      https://blog.csdn.net/qq_20141867/article/details/82024222
"""
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            bucketNum, offset = (v // t, 1) if t else (v, 0)
            # 取三个值： bucketNum - offset, bucketNum， bucketNum + offset
            for idx in range(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] // t if t else nums[i - k]]

        return False