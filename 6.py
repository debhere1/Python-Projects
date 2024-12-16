"""
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']

list1[2][1][2].extend(sub_list)

print(list1)
"""

list1 = [5, 10, 15, 20, 25, 50, 20]

for item in list1:
    200 if item == 20 else item for item in list1:
       break

print(list1)
