import sys, mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    w = int(sys.argv[2])

    c = seq[:w].count('C')
    g = seq[:w].count('G')

    for i in range(len(seq) - w + 1):
        comp = (c + g) / w
        skew = (g - c) / (g + c) if (g + c) else 0
        print(comp, skew)

        if i + w == len(seq): break

        if seq[i]   == 'C': c -= 1
        if seq[i]   == 'G': g -= 1
        if seq[i+w] == 'C': c += 1
        if seq[i+w] == 'G': g += 1


'''import sys
import mcb185

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    w = int(sys.argv[2])
    s = seq[:w]
    c = s.count('C')
    g = s.count('G')
    for i in range(len(seq) -w +1):
        if i != 0:
            if   seq[i-1] == 'C': c -= 1
            elif seq[i-1] == 'G': g -= 1
            if   seq[i+w-1] == 'C': c += 1
            elif seq[i+w-1] == 'G': g += 1
        comp = (c+g) / len(s)
        skew = 0
        if c + g != 0:
            skew = (g-c) / (g+c)
        print(comp, skew)'''