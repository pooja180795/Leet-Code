class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while 0 in nums1 and n > 0:
            nums1.remove(0)
            n -= 1
        nums1.extend(nums2)
        nums1.sort()
        
