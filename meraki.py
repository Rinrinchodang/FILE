f=open("count-people1.exercise.txt","r")
a=f.readlines()
print(len(a))
f.write("rishabh - meerut\nimtiyaz - delhinilima - cochin\nrati -shimla\nayishah - delhi\nraghu - shimla\nnaseer - kanpur\nkarthikeyan - delhi\nsalma - jaipur\npankaj - delhi\nbrijesh - delhi\ngovind - delhi\npuneet - shimla\nsiddhi - delhi\nsuman - jaipur\nrajeev -shimla\nmohinder - delhi\nrajendra - jaipur\npriyanka - shimla\nneela -delhi,sashi - jaipur\nsarika - delhi\ndeepti - shimla\nharshad -delhi\ntrishna - raipur\npradeep - jaipur\nsekhar - delhi\nnand -delhi\nanoop - delhi\nbalwinder - tokyo\n")

f=open("m2count.txt","r")
c=0
for i in f:
    if i!="":
        c=c+1
print("count is ",c)