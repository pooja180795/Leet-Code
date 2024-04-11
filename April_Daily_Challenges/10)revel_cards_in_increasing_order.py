from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        queue = deque()

        # Create a queue of indexes
        for i in range(N):
            queue.append(i)
        
        deck.sort()

        # Put cards at correct index in result
        result = [0] * N
        for card in deck:
            # Reveal Card
            result[queue.popleft()] = card

            # Move next card to bottom
            if queue:
                queue.append(queue.popleft())
                
        return result
    
sol_obj = Solution()
print(sol_obj.deckRevealedIncreasing([17,13,11,2,3,5,7]))
        