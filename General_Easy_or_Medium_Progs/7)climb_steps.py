steps = 3
num1 = 0
num2 = 1

for i in range(1,steps+1):
    next_num  = num1 + num2
    num1 = num2
    num2 = next_num
print(next_num)