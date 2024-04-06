class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        arr= sorted(nums)
        min = arr[0]
        max = arr[-1]
        right, left, count = 0, 0, 0

        for num in nums:
            if num == min or num == max:
                right += 1



sol_obj = Solution()
sol_obj.countSubarrays([5,4,3,2,1], 5, 1)
        