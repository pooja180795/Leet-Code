import re
from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack_folder = []
        pattern = r'^[0-9a-z]'
        for sym in logs:
            if re.match(pattern, sym):
                stack_folder.append(sym)
            elif sym == "../":
                if len(stack_folder) > 0:
                    stack_folder.pop()
                
        
        
        return len(stack_folder)
    
sol_obj = Solution()
print(sol_obj.minOperations(["d1/","d2/","./","d3/","../","d31/"]))