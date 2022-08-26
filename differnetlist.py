# f=open("question.txt","x")
# f.create()
# f.close

delhi=open("del.txt","a")
meerut=open("mee.txt","a")
shimla=open("shim.txt","a")
cochin=open("coc.txt","a")
jaipur=open("jai.txt","a")
tokyo=open("tok.txt","a")
kanpur=open("kan.txt","a")
raipur=open("rai.txt","a")
f=open("question.txt","r")
a=f.read()
b=a.split("\n")
i=0
while i<len(b):
    if "delhi" in b[i]:
        delhi.write(b[i])
        delhi.write("\n")
    elif "meerut" in b[i]:
        meerut.write(b[i])
        meerut.write("\n")
    elif "shimla" in b[i]:
        shimla.write(b[i])
        shimla.write("\n")
    elif "cochin" in b[i]:
        cochin.write(b[i])
        cochin.write("\n")
    elif "jaipur" in b[i]:
        jaipur.write(b[i])
        jaipur.write("\n")
    elif "tokyo" in b[i]:
        tokyo.write(b[i])
        tokyo.write("\n")
    elif "kanpur" in b[i]:
        kanpur.write(b[i])
        kanpur.write("\n")
    else:
        raipur.write(b[i])
        raipur.write("\n")
    i+=1
f.close
