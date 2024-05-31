def performbubblesort(nums):
    n = len(nums)
    fixthisindex = n - 1
    while fixthisindex > 0:
        for index in range(fixthisindex):
            if nums[index] > nums[index + 1]:
                temp = nums[index]
                nums[index] = nums[index + 1]
                nums[index + 1] = temp
        print(nums)
        fixthisindex -= 1
nums = [10,6,55,8,4,11,22,65]
print("before sorting:",nums)
performbubblesort(nums)
print("after sorting:",nums)
