"""number = 10000

for i in range(1,number+1):
    if i * i == number:
        print(number,'is a perfect square as',i,'*',i,'=',number)"""
given_number = 43
needed_list = list()
for i in range(1, given_number):
    list_element = i * i
    if list_element < given_number:
        needed_list.append(list_element)
print(needed_list , reverse=True)
