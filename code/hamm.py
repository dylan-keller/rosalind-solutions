print("Enter two equal length DNA strands")
s1 = input().strip()
s2 = input().strip()

if len(s1)!=len(s2) : 
    print (-1)
    exit()

hamm=0
for i in range(0,len(s1)):
    if s1[i]!=s2[i] : hamm+=1

print(hamm)