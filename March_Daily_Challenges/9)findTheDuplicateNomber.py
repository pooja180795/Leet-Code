class Solution:
    def findDuplicate(self, nums):
        needed_dict = dict()
        for i in nums:
            needed_dict[i] = needed_dict.get(i, 0) + 1
        for k, v in needed_dict.items():
            if v >= 2:
                return k

sol_obj = Solution()
print(sol_obj.findDuplicate([2,1,3,3]))