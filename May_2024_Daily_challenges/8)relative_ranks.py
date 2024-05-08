class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = []
        needed_dict = {}
        needed_arr = sorted(score, reverse= True)
        count = 1
        for i in needed_arr:
            if count == 1:
                needed_dict[i] = "Gold Medal"
                count += 1
            elif count == 2:
                needed_dict[i] = "Silver Medal"
                count += 1
            elif count == 3:
                needed_dict[i] = "Bronze Medal"
                count += 1
            else:
                needed_dict[i] = str(count)
                count += 1
        for i in score:
            answer.append(needed_dict[i])
        return answer
        
sol_obj = Solution()
print(sol_obj.findRelativeRanks([5,4,3,2,1]))