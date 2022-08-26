# f=open("file.size","x")
# f.create()
# f.close

f=open("file.size")
print(f.read())
print("file size is:",f.tell(),"bytes")
