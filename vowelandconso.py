# f=open("vowel.txt","x")
# f.create()
# f.close

# f=open("vowel.txt","w")
# f.write("he is a good boy and he respect everyone")
# f.close

f=open("vowel.txt","r")
x=f.read()
print(x)
vowel=0
consonant=0
i=0
while i<len(x):
    if x[i] in ("a","e","i","o","u","A","E","I","O","U"):
        vowel+=1
    elif (x[i])in ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"):
        consonant+=1
    i+=1
print("vowel:",vowel)
print("consonant:",consonant)
f.close