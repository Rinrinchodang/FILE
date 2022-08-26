# f=open("T.txt","x")
# f.create()
# f.close

# f=open("T.txt","w")
# f.write("My name is Worrin Chodang")
# f.close

f=open("T.txt","r")
x=f.readline()
print(x)
i=0
# a=[]
# b=[]
upper=0
lower=0
while i<len(x):
    if x[i].isupper():
        # a.append(x[i])
        upper+=1
    elif x[i].islower():
        # b.append(x[i])
        lower+=1
    i+=1
print("upper:",upper)
print("lower:",lower)
f.close