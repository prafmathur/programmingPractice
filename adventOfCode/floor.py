paperNeeded = 0
ribbonNeeded = 0
with open('input.txt', 'rU') as f:
  for line in f:
     strings = line.split("x")
     d = sorted([int(i) for i in strings])
     paperNeeded += (3 * d[0] * d[1]) + (2 * d[1] * d[2]) + (2 * d[0] * d[2])
     ribbonNeeded += (d[0] * d[1] * d[2]) + d[0] * 2 + d[1] * 2

print paperNeeded
print ribbonNeeded
