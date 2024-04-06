class Solution:
    def makeGood(self, s: str) -> str:
        my_list = list()
        great_str = str()
        for char in s:
            curr_ascii = ord(char)
            count = len(my_list)
            if count == 0:
                my_list.append(char)
                prev_ascii = curr_ascii


            elif curr_ascii + 32 == prev_ascii or curr_ascii - 32 == prev_ascii:
                my_list.pop()
                #print(my_list)
                if my_list:
                    prev_ascii = ord(my_list[-1])
               
            
            else:
                my_list.append(char)
                prev_ascii = curr_ascii
            
        for i in my_list:
            great_str += i
        
        return great_str

sol_obj = Solution()
print(sol_obj.makeGood("abBAcC"))   