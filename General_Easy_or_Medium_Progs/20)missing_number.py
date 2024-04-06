'''class solution:
    def missing_number(self, nums):
        self.n = len(nums)
        nums = sorted(nums)
      #  return nums

        for self.i in nums:
            if self.i+1 - self.i != 1:
                return self.i

                

    
        
obj = solution()
print(obj.missing_number([0,1,2,4]))'''

nums = [1]
n = len(nums)
nums = sorted(nums)
      #  return nums
if n == 1:
    if nums[0] == 1:
        print(0)
    if nums[0] == 0:
        print(1)
elif nums[0] != 0:
    print(0)
elif nums[n-1] != n:
    print(n)
else:
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] != 1:
            print(nums[i]+ 1)
    