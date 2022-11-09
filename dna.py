import sys

for line in sys.stdin:
    dna = line.strip()
    for i in 'ACGT':
        print(dna.count(i),'', end='')
    break