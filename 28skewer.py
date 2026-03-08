import mcb185
import sequence
import sys

for deline, seq in mcb185.read_fasta(sys.argv[1]):
    window = int(sys.argv[2])
    for i in range(len(seq) - window +1):
        s = seq[i:i+window]
        print(sequence.gc_comp(s), sequence.gc_skew(s))