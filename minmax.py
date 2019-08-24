f = open("studentdata.txt", "r")

for aline in f:
    items = aline.split()
    print(items[0], "max is", max(items[1:]), "min is", min(items[1:]))

f.close()