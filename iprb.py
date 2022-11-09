input=input().strip().split()
p=[int(input[0]),int(input[1]),int(input[2])]
all = sum(p)

# let's calculate the complement, it's easier

# assuming all three integers are >=2 :

complement = 1  *  (p[2]/all)*((p[2]-1)/(all-1)) # 2 homozygous recessive
complement+= (1/4)*(p[1]/all)*((p[1]-1)/(all-1)) # 2 heterozygous
complement+= (1/2)*(p[2]/all)*((p[1])/(all-1)) # 1 hetero 1 homo rec
complement+= (1/2)*(p[1]/all)*((p[2])/(all-1)) # 1 homo rec 1 hetero

print(all)
print(1-complement)