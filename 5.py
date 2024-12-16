list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

list2 = []

for item in list1:
    if item != "":
        list2.append(item)

print(list2)