'''heights = [1,5,1,2,3,4,10000]
bricks = 4
lader = 1


for i in range(len(heights)-1):
    
        if i == len(heights) - 1:
            ans = i
            break

        elif heights[i] > heights[i+1]:
            continue

        elif (bricks > 0 or lader > 0):
            if heights[i+1] - heights[i] <= bricks:
                needed_bricks = heights[i+1] - heights[i]
                bricks = bricks - needed_bricks
                continue
        
            else:
                lader = lader - 1
                continue
            
        else:
            ans = i
            break
    
print(ans)'''

heights = [1,5,1,2,3,4,10000]
bricks = 4
ladders = 1

def furthestBuilding(heights, bricks, ladders):
    def can_reach_end(k):
        nonlocal heights, bricks, ladders

        gaps = [max(0, heights[i + 1] - heights[i]) for i in range(k)]
        gaps.sort(reverse=True)

        for i in range(ladders):
            if i >= len(gaps):
                break
            if gaps[i] > 0:
                continue
            return True

        remaining_bricks = bricks
        for i in range(ladders, k):
            remaining_bricks -= gaps[i]
            if remaining_bricks < 0:
                return False
        return True

    left, right = 0, len(heights) - 1

    while left < right:
        mid = (left + right + 1) // 2
        if can_reach_end(mid):
            left = mid
        else:
            right = mid - 1

    return left

print(furthestBuilding(heights, bricks, ladders))


            
            
    
