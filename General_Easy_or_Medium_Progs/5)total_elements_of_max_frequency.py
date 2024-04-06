my_list = [1,1,32,1,32,32,32,1]
my_dict = dict()
max_frequent_ele = None

for i in my_list:
    my_dict[i] = my_dict.get(i, 0) + 1
print(my_dict)

for i,v in my_dict.items():
    if max_frequent_ele is None or v > max_frequent_ele:
        max_frequent_ele = v
    elif v is max_frequent_ele:
        max_frequent_ele = max_frequent_ele + v
print(max_frequent_ele)
        
