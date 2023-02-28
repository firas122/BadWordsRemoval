import os
import re
import flask
from flask import request

app = flask.Flask(__name__)
@app.route('/do', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        p = request.form.get('string')
        c = request.form.get('string')
        op = request.form.get('string')
        r = p.split(" ")
    k = "r'[z,Z]{1}[e,E]+[b,B]+[i,I]*|[m,M]+[a,A]+[k,K]+[7]+[o,O]+[U,u]+[t,T]{1}|[m,M]*[n,N]{1}[a,A]+[y,Y]+[e,E]*[k,K]+[a,A]*|[3]{0,1}[a,A]+[s,S]+[b,B]+[a,A]+|[m,M]{1}[i,I]+[b,B]+[o,O]+[u,U]+[n,N]+|[W,w]{1}[a,A]+[b,B]+[n,N]+[a,A]+|[k,k]+[a,A]+[7]+[t,T]+[a,A]+|[k,k]+[a,A]+[b,B]+[o,O]+[U,u]+[l,L]+|[z,Z]+[a,A]+[b,B]+[o,O]+[U,u]+[R,r]+[a,A]*|[z,Z]+[b,B]+[a,A]+[R,r]+'"
    for i in range(len(r)):
        searchObj1 = re.search(r'[z,Z]{1}[e,E]+[b,B]+[i,I]*', r[i])
        searchObj2 = re.search(r'[m,M]*[n,N]{1}[a,A]+[y,Y]+[e,E]*[k,K]+[a,A]*', r[i])
        searchObj3 = re.search(r'[3]{0,1}[a,A]+[s,S]+[b,B]+[a,A]+', r[i])
        searchObj5 = re.search(r'[m,M]+[i,I]+[b,B]+[o,O]+[u,U]+[n,N]+', r[i])
        searchObj6 = re.search(r'[W,w]+[a,A]+[b,B]+[n,N]+[a,A]+', r[i])
        searchObj7 = re.search(r'[m,M]+[a,A]+[k,K]+[7]+[o,O]+[U,u]+[t,T]{1}', r[i])
        searchObj8 = re.search(r'[k,K]+[a,A]+[7]+[t,T]+[a,A]+', r[i])
        searchObj9 = re.search(r'[k,K]+[a,A]+[b,B]+[o,O]+[U,u]+[l,L]+', r[i])
        searchObj10 = re.search(r'[z,Z]+[a,A]+[b,B]+[o,O]+[U,u]+[R,r]+[a,A]*', r[i])
        searchObj11 = re.search(r'[z,Z]+[b,B]+[a,A]+[R,r]+', r[i])
        searchObj12 = re.search(r'[n,N]+[a,A]+[m,M]+|[9]+[a,A]+[7,h,H]+[b,B]+[a,A]+|[9]+[a,A]+[7,h,H]+[b,B]+[o,O]+[u,U]+[n,N]+', r[i])


        if searchObj1 or searchObj2 or  searchObj3 or searchObj5 or searchObj6 or searchObj7 or searchObj8 or searchObj9 or searchObj10 or searchObj11 or searchObj12:
            if op == "rp":
                s = "*"*len(r[i])
                r[i] = s
            elif op == "rm":
                r[i] = ""
            else:
                return {"error": "invalid param op"}


    str = ' '
    return{"res": str.join(r)}
port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=port, debug=True)
