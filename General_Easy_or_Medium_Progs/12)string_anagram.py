words = ["a"]
words_dict = {}
#print(dir(my_str))
list = list()
for word in words:
    key = "".join(sorted(word))
    
    if key not in words_dict:
        words_dict[key] = [word]
    else:
        words_dict[key].append(word)
#print(words_dict)
for key, value in words_dict.items():
    list.append(value)
print(list)

    
    