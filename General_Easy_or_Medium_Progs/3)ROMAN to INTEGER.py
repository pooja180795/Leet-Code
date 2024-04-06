# ROMAN to INTEGER
r_n = 'XIV'
if 'IV' in r_n:
    r_n = r_n.replace("IV", "IIII")
if 'IX' in r_n:
    r_n = r_n.replace('IX', 'VIIII')
if 'XL' in r_n:
    r_n = r_n.replace('XL', 'XXXX')
if 'XC' in r_n:
    r_n = r_n.replace('XC', 'LXXXX')
if 'IV' in r_n:
    r_n = r_n.replace('CD', 'CCCC')
if 'CM' in r_n:
    r_n = r_n.replace('CM', 'DCCCC')

i_n = 0

for i in r_n:
    if i == 'I':
        i = 1
    elif i == 'V':
        i = 5
    elif i == 'X':
        i = 10
    elif i == 'L':
        i = 50
    elif i == 'C':
        i = 100
    elif i == 'D':
        i = 500
    elif i == 'M':
        i = 1000

    i_n = i_n + i
print(i_n)
