class NSum:
    def nSum(self, N, nums, target):
        nums.sort()
        res = []
        if N < 2:
            return nums
        elif N == 2:
            lst = []
            for i in range(len(nums)):
                if target - nums[i] in lst:
                    if [target - nums[i], nums[i]] not in res:
                        res.append([target - nums[i], nums[i]])
                lst.append(nums[i])
            return res
        else:
            for i in range(len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                lst = self.nSum(N-1, nums[i+1:], target - nums[i])
                for item in lst:
                    if item:
                        item.insert(0, nums[i])
                        if item not in res:
                            res.append(item)
            return res

if __name__ == "__main__":
    N = 4
    nums = [0, 0, 0, 0]
    target = 0
    nSum = NSum()
    res = nSum.nSum(N, nums, target)
    print(res)

