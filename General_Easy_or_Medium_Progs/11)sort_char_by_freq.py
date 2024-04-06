s = "Aabb"
#print(dir(s))
dict = dict()

for i  in s:
    dict[i] = dict.get(i, 0) + 1
s_list = list()
for k, v in dict.items():
    s_list.append((v, k))
reversed_list = sorted(s_list, reverse=True)
print(reversed_list)
str = ''
for k, v in reversed_list:
    for i in range(k):
        str = str + v
print(str)






