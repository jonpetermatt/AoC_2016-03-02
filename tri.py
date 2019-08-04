import sys

counter = 0
lines = (sys.argv[1]).splitlines()
i = 1
while i < len(lines):
    line0 = lines[i-1].split()
    line1 = lines[i].split()
    line2 = lines[i+1].split()
    j = 0
    while j < 3:
        side0 = line0[j]
        side1 = line1[j]
        side2 = line2[j]
        if (int(side0) + int(side1)) > int(side2):
            if (int(side0) + int(side2)) > int(side1):
                if (int(side1) + int(side2)) > int(side0):
                    counter = counter + 1
        j = j + 1
    i = i + 3

print(counter)
