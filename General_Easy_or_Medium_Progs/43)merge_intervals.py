'''
Problem: Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def merge(self, intervals):
        merged_list = []
        intervals.sort(key=lambda x:x[0])
        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                merged_list.append(prev)
                prev = interval
        merged_list.append(prev)
        return merged_list
    
sol_obj = Solution()
print(sol_obj.merge([[1,99],[92,67],[65,76],[15,18]]))