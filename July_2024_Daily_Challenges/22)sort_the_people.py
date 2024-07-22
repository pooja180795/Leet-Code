from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people_dict = {}
        ans_arr = []
        
        for i in range(len(heights)):
            people_dict[heights[i]] = names[i]
        
        heights.sort(reverse = True)
        
        for height in heights:
            ans_arr.append(people_dict[height])
            
        return ans_arr

sol_obj = Solution()
print(sol_obj.sortPeople(["Abhishek", "Mansi", "Aditya", "Pooja", "Pranav"], [170, 161, 163, 160, 165]))