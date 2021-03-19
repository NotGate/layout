"""
This is a modified version of the generator used to create isrt and a few other layouts
It's not meant to be user-friendly or readable, but I'm posting it anyway for those who are curious
"""

import os
import random
import numpy as np
import math
from itertools import tee, combinations
from collections import Counter
from tqdm import tqdm

# pretty print layout (just ignore this)
def p(c):
    for i in range(0, len(c), 3):
        print(i//3, end='    ')
    print()
    for i in range(len(c)):
        j = i*3 % 30+i//10
        print(c[j], end='    ')
        if (i+1) % 10 == 0:
            print(
                f' {100.0*sum([char_dist[w] for k,w in enumerate(c[i//10::3])])/sum([char_dist[ch] for ch in c]):04.1f}')
    for i in range(0, len(c), 3):
        print(
            f'{100.0*sum([char_dist[w] for k,w in enumerate(c[i:i+3])])/sum([char_dist[ch] for ch in c]):04.1f} ', end='')
    print()
    for i in range(0, len(c), 15):
        print(
            f'{100.0*sum([char_dist[w] for k,w in enumerate(c[i:i+15])])/sum([char_dist[ch] for ch in c]):04.1f} ', end='')
    print()

# sliding window functions are nice for collecting bigrams and trigrams
def window(iterable, size):
    iters = tee(iterable, size)
    for i in range(1, size):
        for each in iters[i:]:
            next(each, None)
    return zip(*iters)

# chunks are good for collecting columns
def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# shuffle the letters
def shuffle(c):
    t = list(c)
    random.shuffle(t)
    return ''.join(t)

# swap 0-N letters
def swap(c, N):
    c = list(c)
    for _ in range(N):
        i = random.randrange(0, 30)
        j = random.randrange(0, 30)
        c[i], c[j] = c[j], c[i]
    return ''.join(c)

# get usage of a column (enforcing high index usage)
def pop(z, zz):
    return sum([char_dist[ch] for ch in z])/sum([char_dist[ch] for ch in zz])

# sum up the SFBs
# you can experiement with scalars for the bi_dist and tri_dist for inner and outer columns
def cost(c):
    s = 0
    # sides
    for (i, col) in enumerate(chunks(c, 3)):
        if i not in [3, 4, 5, 6]:
            for b in combinations(col, 2):
                s += bi_dist[b[0]+b[1] if b[0] < b[1] else b[1]+b[0]] \
                    # + tri_dist[b[0]+b[1] if b[0] < b[1] else b[1]+b[0]]
    # indexes
    for b in combinations(c[9:15], 2):
        s += bi_dist[b[0]+b[1] if b[0] < b[1] else b[1]+b[0]] \
                    # + tri_dist[b[0]+b[1] if b[0] < b[1] else b[1]+b[0]]
    for b in combinations(c[15:21], 2):
        s += bi_dist[b[0]+b[1] if b[0] < b[1] else b[1]+b[0]] \
                    # + tri_dist[b[0]+b[1] if b[0] < b[1] else b[1]+b[0]]
    return s

def get_text(t):
    text = [c for c in open(f"data/{t}.txt").read().lower()]
    text = [';' if c == ':' else c for c in text]   # hard-coded cringe
    text = ['\'' if c == '"' else c for c in text]  # hard-coded cringe
    text = ['/' if c == '?' else c for c in text]   # hard-coded cringe
    return ''.join(text)  

# treating bi_dists (somewhat) equally
def normalize2(d1,d2):
    I, J = sum(d1.values()), sum(d2.values())
    N = I + J
    d = dict()
    for key in set(list(d1.keys())+list(d2.keys())):
        d[key] = int(N*(d1.get(key,0)/I + d2.get(key,0)/J))
    return d
    
def normalize3(d1,d2,d3):
    return normalize2(normalize2(d1,d2),d3)

text1 = get_text("quotes")
text2 = get_text("books")
text3 = get_text("1k")

bigrams1 = [a+b if a < b else b+a for (a, b) in window(''.join(text1), 2)]
bigrams2 = [a+b if a < b else b+a for (a, b) in window(''.join(text2), 2)]
bigrams3 = [a+b if a < b else b+a for (a, b) in window(''.join(text3), 2)]

# for (b,v) in Counter(bigrams2).most_common(10000):
#     if ' ' not in b and '\n' not in b and b[0].isascii() and b[1].isascii():
#         print(b,v)
# exit()

# decided just to care about trigrams for quotes, since it's more of a light heuristic
trigrams = [a+c if a < c else c+a for (a, _, c) in window(''.join(text1), 3)]

char_dist = Counter(text1)
bi_dist = Counter(normalize3(Counter(bigrams1),Counter(bigrams2),Counter(bigrams3)))
tri_dist = Counter(trigrams)

N = 10000
M = 100 # set to 1k+ depending on the complexity of the cost function
results = []
for _ in tqdm(range(M)):
    layout = shuffle('abcdefghijklmnopqrstuvwxyz.,;\'')
    score = cost(layout)
    for i in range(N):
        layout_ = swap(layout, int(float(N-i)/float(N) * 5.0) + 1)
        score_ = cost(layout_)
        # you can go nuts with this if-statement and hard-code whatever you're looking for
        if score_ <= score and pop(layout_[9:15], layout_) > 0.13 and pop(layout_[9:15], layout_) < 0.19 and pop(layout_[15:21], layout_) > 0.13 and pop(layout_[15:21], layout_) < 0.19:
            layout = layout_
            score = score_
    if pop(layout[9:15], layout) > 0.13 and pop(layout[9:15], layout) < 0.19 and pop(layout[15:21], layout) > 0.13 and pop(layout[15:21], layout) < 0.19:
        results.append((score, layout))

# You'll still have to move around some of the rows and columns
# Writing the code for that is annoying
for (score, layout) in sorted(results, key=lambda pair: pair[0], reverse=False)[:10]:
    layout = [''.join(sorted(layout[i:i+3], key=lambda s: char_dist[s], reverse=True))
              for i in range(0, len(layout), 3)]
    layout = ''.join([w[1]+w[0]+w[2] for w in layout])
    print(f'{score} {layout}')
    p(layout)
    print()


""" 
y    m    u    o    .    p    w    h    f    '
i    t    e    a    ,    g    d    n    s    r
j    k    z    q    ;    b    c    l    v    x

e 1189270
t 857621
a 772047
o 743158
i 664716
n 659446
h 601534
s 600522
r 551354
d 428936
l 395151
u 278222
m 257890
w 230357
c 228885
f 208786
y 202083
g 192882
, 183054
p 158583
b 149480
. 115106
' 102905
v 91308
k 78419
; 29250
- 24815
? 14944
j 14421
x 14308
! 11258
q 10285
z 6129
"""
