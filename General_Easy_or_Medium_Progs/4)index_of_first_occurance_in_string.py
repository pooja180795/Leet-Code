given_str = "kklklklklklpooja"
needle = "pooja"

if needle in given_str:
    #print("yes")
    just_b4_word = given_str.split(needle)
    #print(just_b4_word)
    index_of_first_needle = len(just_b4_word[0])
    print("index is",index_of_first_needle)
else:
    print("no")