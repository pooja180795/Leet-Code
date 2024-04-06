words = ["ttfr","abaki","ada","asdsa"]
count = 0
for i in words:
    if count == 1:
        break
    elif len(i) % 2 == 1:
        limit = int(len(i)/2)
        #print(limit)
        end_pos = len(i) - 1
        for start_pos in range(0, limit):
            if i[start_pos] == i[end_pos]:
                end_pos = end_pos - 1
                if start_pos + 1 == end_pos:
                    print(i)
                    count = count + 1

            else:
                break
