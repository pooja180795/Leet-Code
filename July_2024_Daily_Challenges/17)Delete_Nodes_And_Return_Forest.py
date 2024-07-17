'''
question Name : Delete Nodes And Return Forest
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDeleteSet = set(to_delete)
        forestList = []
        
        root = self._postOrder(root, toDeleteSet, forestList)
        
        if root:
            forestList.append(root)
        return forestList
        
    def _postOrder(self, node, toDeleteSet, forestList):
        if not node:
            return None
        
        node.left = self._postOrder(node.left, toDeleteSet, forestList)
        node.right = self._postOrder(node.right, toDeleteSet, forestList)
            
        if node.val in toDeleteSet:
                
            if node.left:
                forestList.append(node.left)
            if node.right:
                forestList.append(node.right)
            
            return None
        return node