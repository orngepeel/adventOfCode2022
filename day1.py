f = open(r"input.txt", "r")

lines = f.readlines()

totals = []

current_total = 0

for line in lines:

    if line == "\n":
        totals.append(current_total)
        current_total = 0
        continue

    stripped = line.strip()
    current_total += int(stripped)

# Part 1
print(max(totals))

# Part 2
print(sum(sorted(totals, reverse=True)[0:3]))
