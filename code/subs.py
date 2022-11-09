"""
SUBS : Finding a Motif in DNA 

Given: 
Two DNA strings s and t (each of length at most 1 kbp).
Return: 
All locations of t as a substring of s.
"""

with open("../data/rosalind_subs.txt", 'r') as txt_file:
    s = txt_file.readline().strip()
    t = txt_file.readline().strip()

if len(t) > len(s) : exit()

locations=[]

for i in range(0, len(s)-len(t)):
    if t == s[i:i+len(t)] : locations.append(i+1)

for i in locations:
    print(i, end=" ")