# f=open("end","x")
# f.create()
# f.close

# f=open("end","w")
# f.write("she is sing")
# f.close

# f=open("end","r")
# # a=f.readlines()
# # i=0
# c=0
# for i in f:
# # while i<len(a):
#     if i=="ing":
#         c+=1
# print("the count is",c)

f=open("end","r")
a=f.read()
print(a)
x=a.split()
i=0
c=0
while i<len(x):
    if "ing" in x[i]:
        c+=1
    i+=1
print("the count is",c)
f.close
