import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            word = line.split()
            if word[2] == 'CDS':
                beg = int(word[3])
                end = int(word[4])
                print(end-beg + 1)
