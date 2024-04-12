class Solution:
    def majorityElement(self, nums) -> int:
        my_dict = dict()
        max = 0
        for i in nums:
            my_dict[i] = my_dict.get(i, 0) + 1
        #print(my_dict)
        for k, v in my_dict.items():
            if v > max:
                max = v
                key = k
        return key
    
sol_obj = Solution()
print(sol_obj.majorityElement([2,2,1,1,1,2,2,2, 8,8,8,8,8,8,8,8]))