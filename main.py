import re

klem = ["zebi","3asba","nayek","zebi"]
r = "barra nayek 3a zebbbbbbbbiiii"
r = r.split(" ")


for i in range(len(r)):
    searchObj = re.match(r'[z]{1}[e]{1}[b]*[i]*', r[i])
    if searchObj:
        s = "*"*len(r[i])
        r[i]=s

str = ' '
print(str.join(r))