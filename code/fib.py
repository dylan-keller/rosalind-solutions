"""
FIB : Rabbits and Recurrence Relations 

Given: 
Positive integers n≤40 and k≤5
Return: 
The total number of rabbit pairs that will be present after n months, 
if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

def fib(n,k):
    if n==0 : return 0
    if n==1 : return 1
    a,b=0,1
    for i in range (2,n+1) :
        a,b=b,b+k*a
    return b

with open("../data/rosalind_fib.txt", 'r') as txt_file:
    n_k = txt_file.readline().strip()
    nk=n_k.split()
    print(fib(int(nk[0]), int(nk[1])))