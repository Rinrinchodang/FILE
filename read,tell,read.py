f=open("my-file.txt")
f.seek(3)
f1=f.read()
print(f1)
f2=f.tell()
print(f2)
f.close

# f=open("my-file.txt","w")
# f.write("hello")
# f.close