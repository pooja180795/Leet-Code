'''
Problem Name: distribute coins in binary tree
You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def dfs(current):
            if current is None: return 0
            
            left_coins = dfs(current.left)
            right_coins = dfs(current.right)

            self.moves += abs(left_coins) + abs(right_coins)

            return current.val - 1 + left_coins + right_coins

        dfs(root)
        return self.moves
        