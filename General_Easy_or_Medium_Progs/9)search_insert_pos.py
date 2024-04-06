array1 = [1,3,5,7,9]
num = 4

for i in range(len(array1)):
    if array1[i] < num:
        if i < len(array1) - 1:
            continue
        pos = i + 1
        break
    elif array1[i] == num:
        pos = i
        break
    elif array1[i] > num:
        pos = i
        break
print("index of number ",num,"=",pos)
