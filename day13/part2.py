import re

total = 0

with open("input.txt") as file:
    for block in file.read().strip().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
        px += 10000000000000
        py += 10000000000000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += int(ca * 3 + cb)

print(total)