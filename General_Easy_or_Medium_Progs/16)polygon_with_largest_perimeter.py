class polygon:
    nums = [5,15,5]
    nums.sort()
    ans = None

    while len(nums) >= 3:
        if sum(nums) - nums[len(nums) - 1] > nums[len(nums) - 1]:
            ans  = sum(nums)
           # print(ans)
            break
        else:
            nums.pop(len(nums) - 1)
    if ans:
        print(ans)
    else:
        print(-1)





    