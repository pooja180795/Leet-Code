class Solution:
    def findMaxK(self, nums) -> int:
        needed_dict = {}
        for i in nums:
            needed_dict[i] = needed_dict.get(i, 0) + 1
        sorted_dict = dict(sorted(needed_dict.items(), reverse=True))
        for k, v in sorted_dict.items():
            if -k in sorted_dict:
                return k
            else: continue
        return -1
    
sol_obj = Solution()
sol_obj.findMaxK([-1,10,6,7,-7,1])
