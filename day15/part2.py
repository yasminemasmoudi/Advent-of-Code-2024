import sys
import re
from collections import deque
import pyperclip as pc

def pr(s):
    print(s)
    pc.copy(s)

sys.setrecursionlimit(10**6)
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  

def ints(s):
    return [int(x) for x in re.findall('-?\d+', s)]

D = open('input.txt').read().strip()

G, instrs = D.split('\n\n')
G = G.split('\n')

def solve_part2(G, instrs):
    R = len(G)
    C = len(G[0])
    
    G = [[G[r][c] for c in range(C)] for r in range(R)]
    
    BIG_G = []
    for r in range(R):
        row = []
        for c in range(C):
            if G[r][c] == '#':
                row.append('#')
                row.append('#')  # Wall becomes double width
            elif G[r][c] == 'O':
                row.append('[')
                row.append(']')  # Box becomes a double-width box
            elif G[r][c] == '.':
                row.append('.')
                row.append('.')  # Empty space becomes double-width
            elif G[r][c] == '@':
                row.append('@')
                row.append('.')  # Robot becomes double width
        BIG_G.append(row)
    
    G = BIG_G
    C *= 2  # Update column count since the grid is now double the width

    for r in range(R):
        for c in range(C):
            if G[r][c] == '@':
                sr, sc = r, c
                G[r][c] = '.'  

    r, c = sr, sc

    for inst in instrs:
        if inst == '\n':
            continue
        dr, dc = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[inst]

        rr, cc = r + dr, c + dc
        
        if G[rr][cc] == '#':
            continue
        elif G[rr][cc] == '.':
            r, c = rr, cc
        elif G[rr][cc] in ['[', ']', 'O']:
            Q = deque([(r, c)])
            SEEN = set()
            ok = True
            while Q:
                rr, cc = Q.popleft()
                if (rr, cc) in SEEN:
                    continue
                SEEN.add((rr, cc))
                rrr, ccc = rr + dr, cc + dc
                if G[rrr][ccc] == '#':
                    ok = False
                    break
                if G[rrr][ccc] == 'O':
                    Q.append((rrr, ccc))
                if G[rrr][ccc] == '[':
                    Q.append((rrr, ccc))
                    assert G[rrr][ccc + 1] == ']'
                    Q.append((rrr, ccc + 1))
                if G[rrr][ccc] == ']':
                    Q.append((rrr, ccc))
                    assert G[rrr][ccc - 1] == '['
                    Q.append((rrr, ccc - 1))
            if not ok:
                continue
            while len(SEEN) > 0:
                for rr, cc in sorted(SEEN):
                    rrr, ccc = rr + dr, cc + dc
                    if (rrr, ccc) not in SEEN:
                        assert G[rrr][ccc] == '.'
                        G[rrr][ccc] = G[rr][cc]
                        G[rr][cc] = '.'
                        SEEN.remove((rr, cc))
            r = r + dr
            c = c + dc

    ans = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] in ['[', 'O']:  
                ans += 100 * r + c

    return ans

pr(solve_part2(G, instrs))
