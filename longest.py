# f=open("longest.txt","x")
# f.create()
# f.close

f=open("longest.txt","r")
f1=f.read()
word=f1.split()
print(word)
max=word[0]
i=0
while i<len(word):
    if len(word[i])>len(max):
        max=word[i]
    i+=1
print("the longest word is:",max)
f.close