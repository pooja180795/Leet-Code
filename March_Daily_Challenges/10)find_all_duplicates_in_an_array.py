class Solution:
    def findDuplicates(self, nums):
        twised_ele_arr = list()
        nums_dict = dict()
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        print(nums_dict)
    
        for k, v in nums_dict.items():
            if v == 2:
                twised_ele_arr.append(k)
            else:
                continue
        return twised_ele_arr

sol_obj = Solution()
print(sol_obj.findDuplicates([2,1,3,2,3]))
            
            