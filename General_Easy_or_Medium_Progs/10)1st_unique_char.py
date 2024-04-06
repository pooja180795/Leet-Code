my_str = 'lovelove'
my_dict = dict()

for char in my_str:
    my_dict[char] = my_dict.get(char, 0) + 1



for k, v in my_dict.items():
    if v == 1:
        ans = k
        break

try:
    print(my_str.index(ans))
except:
    print('-1') 