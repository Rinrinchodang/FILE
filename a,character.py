# f=open("con.txt","x")
# f.create()
# f.close

# f=open("con.txt","w")
# f.write("worrin\nseminao\nthemsimla\nkatimla\nling\nodette\ngusion\nguinevere\n")
# f.close

list=open("list","a")
list1=open("list1","a")
f=open("con.txt","r")
c=f.readlines()
i=0
while i<len(c):
    if "a" in c[i]:
        list.write(c[i])
    elif "a" not in c[i]:
        list1.write(c[i])
    i+=1
print(list1)
f.close
        