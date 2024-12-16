
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

out = []

for item in list1:
    for n in list2:
        out.append(item + n)

print(out)