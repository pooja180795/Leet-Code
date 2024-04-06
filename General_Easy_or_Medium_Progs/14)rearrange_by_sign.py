#one way
array = [10, 2, 33, -10, -32, -30]
negative_array = list()
positive_array = list()
needed_array = list()
for i in array:
    if i < 0:
        negative_array.append(i)
    if i > 0:
        positive_array.append(i)
for i in range(len(positive_array)):
    
    needed_array.append(positive_array[i])
    needed_array.append(negative_array[i])  
            
print(needed_array)


#other way
'''nums = [1,2,3,-1,-2,-3]
ans = list()
pos_index = 0
neg_index = 1

for i in nums:
    if i > 0:
        ans.insert(pos_index, i)
        pos_index = pos_index + 2
    if i < 0:
        ans.insert(neg_index, i)
        neg_index = neg_index + 2
print(ans)'''




