list = [9,6,9]
list.reverse()

for i in range(len(list)):
    list[i] = list[i] + 1
     
    if list[i] == 10:
        list[i] = 0
        if len(list) == i+1:
            list.append(1)
        continue
    else:
        break
        
list.reverse()
print(list)