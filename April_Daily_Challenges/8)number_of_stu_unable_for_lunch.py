class Solution:
    def numOfStuUnableForLunch(self, students, sandwiches):
        i = 0
        while len(students) > 0:
            if students[i] == sandwiches[i]:
                students.pop(i)
                sandwiches.pop(i)
            else:
                if sandwiches[i] in students:
                    students.append(students[i])
                    students.pop(i)
                else: return (len(students))
        return len(students)





sol_obj = Solution()
print(sol_obj.numOfStuUnableForLunch([0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0]))