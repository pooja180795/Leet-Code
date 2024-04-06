


class Solution:
    def bagOfTokensScore(self, tokens, power: int) -> int:
        tokens = sorted(tokens)
        score = 0
        while tokens:
            if power >= tokens[0]:
                print("hi")
                power = power - tokens[0]
                score += 1
                tokens.remove(tokens[0])

            elif score >= 1 and len(tokens) > 1:
                print("hello")
                max_value = max(tokens)
                power = power + max_value
                score -= 1
                tokens.remove(max_value)

            else: 
                break
            
        return score       

sol_obj = Solution()
print(sol_obj.bagOfTokensScore([1,4,1,1], 1))