class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        starting_pos_stack = list()
        count = -1
        valid_list = list()
        start_bracket_count = 0
        valid_str = str()

        for char in s:
            if char == '(':
                valid_list.append(char)
                count += 1
                start_bracket_count += 1
                starting_pos_stack.append(count)
            elif char == ')':
                if start_bracket_count > 0:
                    valid_list.append(char)
                    count += 1
                    starting_pos_stack.pop()
                    start_bracket_count -= 1
            else:
                valid_list.append(char)
                count += 1
        if start_bracket_count == 0:
            for i in valid_list:
                valid_str += i
            return valid_str

        starting_pos_stack.sort(reverse=True)
        for i  in starting_pos_stack:
            valid_list.pop(i)
        for i in valid_list:
            valid_str += i
        return valid_str
            
                    
                


sol_obj = Solution()
print(sol_obj.minRemoveToMakeValid(")))(("))