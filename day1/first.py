
def first():
    lines = []

    # Read the file and strip newline characters
    with open("input.txt") as file:
        lines = [line.strip() for line in file if line.strip()]
    L1 = []
    L2 = []

    for line in lines:
        parts = line.split()
        L1.append(int(parts[0]))
        L2.append(int(parts[1]))

    L1.sort()
    L2.sort()

    total = 0
    for i in range (len(L1)):
        total += abs(L1[i] - L2[i])    

    print(total)

first()
#2430334 
