def removeDuplicates(nums):
    count = 0
    index = 0
    while index < len(nums) and count < len(nums):
        if index > 0 and nums[index] == nums[index-1]:
            nums.append(nums.pop(index))
        else:
            index += 1
        count += 1
    return nums[:index]

if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,2,3,3,4,5,5,5,6,7,8,8]
    res = removeDuplicates(nums)
    print(res)