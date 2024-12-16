
fhand = open("mbox-short.txt")
days = {}

for line in fhand:
    if line.startswith("From "):
        day = line.split()[2]
        days [day] = days.get(day, 0) + 1

print(days)