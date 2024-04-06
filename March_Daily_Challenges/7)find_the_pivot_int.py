class Solution:
    def pivotInteger(self, n: int) -> int:
        m =  [i for i in range(1, n+1)]
        left = m[0]
        right = 0
        for i in m:
            right = right + i
        if left == right:
            return left
        else:
            for i in range(m[1], n+1):
                left = left + i
                right = right - m[i-2]
                if left == right:
                    return i
            return -1
                
sol_obj = Solution() 
print(sol_obj.pivotInteger(8))