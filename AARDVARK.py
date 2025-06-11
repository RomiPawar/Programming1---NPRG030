import sys
import collections

freqs = collections.defaultdict(lambda: collections.defaultdict(int))

for line in sys.stdin:
    word = ''
    for c in line.lower():
        if 'a' <= c <= 'z':
            word += c
        elif word != '':
            freqs[len(word)][word]+=1
            word = ''

for l, freq in sorted(freqs.items()):
    top = max(freq.values())
    words = ' '.join(sorted(w for w, f in freq.items() if f == top))
    s = '' if top == 1 else 's'
    print(f'length {l}: {words} ({top} occurrence{s})')
