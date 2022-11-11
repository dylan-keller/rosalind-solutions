"""
PROT : Translating RNA into Protein 

Given: 
An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: 
The protein string encoded by s.
"""
def rna_to_prot(s):
    rna_codon_table = {
        "UUU": 'F', "CUU": 'L', "AUU": 'I', "GUU": 'V',
        "UUC": 'F', "CUC": 'L', "AUC": 'I', "GUC": 'V',
        "UUA": 'L', "CUA": 'L', "AUA": 'I', "GUA": 'V',
        "UUG": 'L', "CUG": 'L', "AUG": 'M', "GUG": 'V',
        "UCU": 'S', "CCU": 'P', "ACU": 'T', "GCU": 'A',
        "UCC": 'S', "CCC": 'P', "ACC": 'T', "GCC": 'A',
        "UCA": 'S', "CCA": 'P', "ACA": 'T', "GCA": 'A',
        "UCG": 'S', "CCG": 'P', "ACG": 'T', "GCG": 'A',
        "UAU": 'Y', "CAU": 'H', "AAU": 'N', "GAU": 'D',
        "UAC": 'Y', "CAC": 'H', "AAC": 'N', "GAC": 'D',
        "UAA": 'x', "CAA": 'Q', "AAA": 'K', "GAA": 'E',
        "UAG": 'x', "CAG": 'Q', "AAG": 'K', "GAG": 'E',
        "UGU": 'C', "CGU": 'R', "AGU": 'S', "GGU": 'G',
        "UGC": 'C', "CGC": 'R', "AGC": 'S', "GGC": 'G',
        "UGA": 'x', "CGA": 'R', "AGA": 'R', "GGA": 'G',
        "UGG": 'W', "CGG": 'R', "AGG": 'R', "GGG": 'G'
    }
    prot=""
    for i in range(0,len(s),3):
        prot+=rna_codon_table[s[i:i+3]]
    return prot[:prot.index('x')]


with open("../data/rosalind_prot.txt", 'r') as txt_file:
    rna_string = txt_file.readline().strip()
print(rna_to_prot(rna_string))