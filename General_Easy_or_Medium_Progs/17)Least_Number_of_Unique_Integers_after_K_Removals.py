
from collections import OrderedDict
arr = [36378,37755,79583,46672,55607,86615,31206,49748,88367,35602,30497,1433,70826,96199,9763,40811]
k = 59169
arr_dict  = dict()
new_arr = list()

for i in arr:
    arr_dict[i] = arr_dict.get(i, 0) + 1

for i, v in arr_dict.items():
    if k > 0:

        if v == 1:
            arr.remove(i)
            k = k - 1
        
        elif v > 1 and v <= k:
            for m in range(0, v):
                arr.remove(i)
                k = k - 1

unique_values = list(OrderedDict.fromkeys(arr))
print(len(unique_values))

