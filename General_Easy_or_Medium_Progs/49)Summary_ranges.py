class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        count = 0
        ans = []
        for i in range(len(nums)):
            if nums[i] + 1 != nums[i+1]:
                if count == 0:
                    ans.append[str(nums[i])]
                else:
                    a = str(start)
                    b = str(nums[i])
                    string = a + "->" + b
                    ans.append[str(string)]
                    count = 0
            else: 
                count += 1
                if count == 1:
                    start = nums[i]
                    
        return ans
                
                    