from typing import Optional

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
       # print(q)
        if not p and not q:
            return True
        if not p or not q:
            return False
        print(p.val)
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        
        


sol = Solution()
p = TreeNode(1,
             TreeNode(2,
                      TreeNode(4),
                      TreeNode(5)),
             TreeNode(3,
                      TreeNode(6),
                      TreeNode(7)))
q = TreeNode(1,
             TreeNode(2,
                      TreeNode(4),
                      TreeNode(5)),
             TreeNode(3,
                      TreeNode(6),
                      TreeNode(7)))

result = sol.isSameTree(p, q)
print(result)