dna = "AGACGTGAATGTACAGAGATGCGCAATTTAGCCGTCTAATTCTCTATTGTAACAGCCGCCCTACATCTGCTTTTCTTGCAATGAGGAATACCATCTTCGGACCTCTACAAGCAGTTCAATTTTTGTTAACCATGTTCGTTTTAGCTGAAGCTGTGTGGTTGAAACGCGGTTACCTTGAGTTCCCGTGGCGCGGACTAATAAGAAATGCGGCTCCCAGGAAGTACTTTGAGACTCAGTTAAGGCATGGTGTTTTACTTGGCAGCACATGTCGGCCGCGTACTAAGTGCCCTTTAGATTGGACGAGCGAGTGACGAGACAAAACTGAACTGACACCATGAGGCAGGCGCTACTTGGGGTCGACGCGGCGAGTGCGTTATCACGACCAATACTTACGTACCGTGCTTCGAGTAGTAGCCACGACGCGCGTTCCTTTGCCGCTAACGACGTCAGCTCTGGACATGTAATACCTATGCCCCTGGTGTTCCACGAAACCAGATTCGCGAACATAGAATCATTCTGTAGTGAGGGCGAACCCAGCATATAGCACCGAATTGGCGTGCTAACTTGCATTTACGTTTAGTGCATGACTGGTAAACAAGGTAATACGCTTGGCCCGCCAATCCAAGTAAGGGAGAGGTGAACTTCGGCGGTAGTGTACGGGCAAGATCGATAGGCGAGGGAGGACGACCCGGGAACGAAGGATGCCAACTGTCTTTGCTGGTTGGACTTCTTGCTTCTAACTCTTCTCAGACTATAACTGCCATGTTCTACCGACTTTAGCGCAATCTATGGTGCACGGCCGGCTGGACAGTACGTTTGTTA"

nba = dna.count('A')
nbc = dna.count('C')
nbg = dna.count('G')
nbt = dna.count('T')

print(nba, nbc, nbg, nbt)