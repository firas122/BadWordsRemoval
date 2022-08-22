import re
inp = input('write your string to clean  : ')
klem = ["3asba","nayek","zebi"]

print(inp)
r = inp.split(" ")


for i in range(len(r)):
    searchObj1 = re.match(r'[z,Z]{1}[e,E]+[b,B]+[i,I]+', r[i])
    searchObj2 = re.match(r'[m,M]*[n,N]{1}[a,A]+[y,Y]+[e,E]+[k,K]+', r[i])
    searchObj3 = re.match(r'[3]{1}[a,A]+[s,S]+[b,B]+[a,A]+', r[i])
    searchObj4 = re.match(r'[3]{1}[a,A]+[s,S]+[b,B]+[a,A]+', r[i])
    searchObj5 = re.match(r'[9]{1}[a,A]+[7]+[b,B]+[a,A]+', r[i])

    if searchObj1 or searchObj2 or  searchObj3 or searchObj4 or searchObj5:
        s = "*"*len(r[i])
        r[i]=s

str = ' '

print(str.join(r))