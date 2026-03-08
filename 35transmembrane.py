import sys
import mcb185

kd = {
'A':1.8,'C':2.5,'D':-3.5,'E':-3.5,'F':2.8,'G':-0.4,'H':-3.2,
'I':4.5,'K':-3.9,'L':3.8,'M':1.9,'N':-3.5,'P':-1.6,'Q':-3.5,
'R':-4.5,'S':-0.8,'T':-0.7,'V':4.2,'W':-0.9,'Y':-1.3
}

def avg_kd(s):
    total = 0
    for aa in s:
        total += kd[aa]
    return total / len(s)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    if len(seq) < 41: continue
    signal = False
    for i in range(30 - 8 + 1):
        s = seq[i:i+8]
        if 'P' in s: continue
        if avg_kd(s) >= 2.5:
            signal = True
            break

    if not signal: continue

    tm = False
    for i in range(30, len(seq) - 11 + 1):
        s = seq[i:i+11]
        if 'P' in s: continue
        if avg_kd(s) >= 2.0:
            tm = True
            break

    if tm:
        print(defline)