print("input dna strand")
strand = input().strip()

def change_str(s,i,c):
    return s[:i] + c + s[i+1:]

for i in range (0, len(strand)) :
    match strand[i]:
        case 'A': strand = change_str(strand,i,'T')
        case 'T': strand = change_str(strand,i,'A')
        case 'C': strand = change_str(strand,i,'G')
        case 'G': strand = change_str(strand,i,'C')

print(strand[::-1])