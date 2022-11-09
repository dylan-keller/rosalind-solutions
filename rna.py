print("input dna strand")
strand = input().strip()

for i in range (0, len(strand)) :
    if (strand[i] == 'T') : strand = strand[:i] + 'U' + strand[i+1:]

print(strand)