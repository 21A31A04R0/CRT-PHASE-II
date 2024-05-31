def performinsertionsort(nums):
    n = len(nums)
    lasteleinsortedsarr = 0
    for firstindex in range(1,n):
        temp = nums[firstindex]
        previous = lasteleinsortedsarr
        
        while previous >= 0 and nums[previous] > temp:
            nums[previous + 1] = nums[previous]
            previous -= 1
        nums[previous + 1] = temp
        lasteleinsortedsarr +=1
nums = [ 10,6,23,7,9]
print("before sorting:",nums)
performinsertionsort(nums)
print("after sorting:",nums)
