class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        needed_boats = 0
        sorted_people = sorted(people)
        i, j = 0, len(people) - 1

        while i <= j:
            if sorted_people[i] + sorted_people[j] <= limit:
                i += 1
            j -= 1
            needed_boats += 1
        return needed_boats

           
sol_obj = Solution()
print(sol_obj.numRescueBoats([5,5,5,5], 5))