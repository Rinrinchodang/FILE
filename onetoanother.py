# f=open("file1.txt","x")
# f.create()
# f.close

# f=open("file2.txt","x")
# f.create()
# f.close

n=int(input("enter the number of lines copied"))
file1=open("file1.txt")
file2=open("file2.txt","w")
contents=file1.readlines()
count=0
for line in contents:
        if count<n:
            file2.write(line)
            count+=1
file2.close