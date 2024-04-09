class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        needed_tkts = tickets[k]
        sec= 0
        while needed_tkts > 0:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    if i == k:
                        needed_tkts -= 1
                    tickets[i] -= 1
                    sec += 1
                    if needed_tkts == 0:
                        return sec
            print(tickets)
        return sec

sol_obj = Solution()
print(sol_obj.timeRequiredToBuy([84,49,5,24,70,77,87,8], 2))