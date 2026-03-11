import json
truc = {
    'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
    'numbers': [1.09, 2.72, 3.14],
    'is_complete': False,
}
print(json.dumps(truc, indent=4))

"""
d = {'dog': 'woof', 'cat': 'meow'}
print(d.keys(), d.values(), list(d.values()))


import gzip

with gzip.open("../MCB185/data/A.thaliana.fa.gz", "rt") as fp:
    for line in fp:
        print(line, end="")


fp = open("21entropy.py")
for line in fp:
    print(line.strip())
fp.close
"""