import string

for l in string.ascii_uppercase:
    if string.ascii_uppercase.index(l) % 2 == 0:
        print(l)