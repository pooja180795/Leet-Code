n = 33

for i in range(0,31):
    if 2 ** i == n:
        print("True")
        break
    elif 2 ** i < n:
        continue
    else:
        print("False")
        break
