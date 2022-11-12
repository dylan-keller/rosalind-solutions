"""
PROT : Computing GC Content
Identifying Unknown DNA Quickly

Given: 
At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: 
The ID of the string having the highest GC-content, followed by the GC-content of that string. 

note: Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.
"""

res_id=""
res_percent=0.0

current_id=""
current_GC=0.0
current_bases=1.0

with open("../data/rosalind_gc.txt", 'r') as txt_file:
    while True :
        current_line = txt_file.readline().strip()
        

        if current_line == "" or current_line[0] == '>' :
            if (current_GC/current_bases) > res_percent :
                res_percent = (current_GC/current_bases)
                res_id = current_id
            current_GC=0
            current_bases=0
            current_id = current_line[1:]
            if current_line == "" : break
        
        else :
            current_GC += current_line.count('C') + current_line.count('G')
            current_bases += len(current_line)

print(res_id)
print(str(res_percent*100)[:9])