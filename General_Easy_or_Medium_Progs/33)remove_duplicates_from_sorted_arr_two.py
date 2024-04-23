class Solution:
    def removeDuplicates(self, nums) -> int:
        index = 1
        occurance = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                occurance += 1
            else:
                occurance = 1
            
            if occurance <= 2:
                nums[index] = nums[i]
                index += 1
        print(nums)
        return index            

        
sol_obj = Solution()
print(sol_obj.removeDuplicates([1,1,1,4,5]))
