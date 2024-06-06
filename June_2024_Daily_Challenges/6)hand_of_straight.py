'''
Problem Statement : Hand of Straights
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
'''
class Solution:
    def isNStraightHand(self, hand, groupSize: int):
        list = sorted(hand)
        if len(list) % groupSize == 0:
            while len(list) > 0:
                i = list[0]
                count = 0
                while count != groupSize:
                    if i in list:
                        list.remove(i)
                        i += 1
                        count += 1
                    else: return False
            return True
            
        else: return False
        
sol_obj = Solution()
print(sol_obj.isNStraightHand([1,2,3,4,5], 4))