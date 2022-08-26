# f=open("count.txt","x")
# f.create()
# f.close

f=open("count.txt","r")
no_of_lines=0
no_of_words=0
no_of_letters=0
for line in f:
    line=line.strip("\n")
    words=line.split()
    no_of_lines+=1
    no_of_words+=len(words)
    no_of_letters+=len(line)
print("no. of line=",no_of_lines)
print("no. of word=",no_of_words)
print("no. of letters",no_of_letters)
f.close
