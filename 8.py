'''
filename = input("Enter a file name: ")
fhand = open(filename, 'r')

#print(fhand.read())
email_address = {}

for line in fhand:
    if line.startswith('From'):
        email = line.split()[1]
        email_address[email] = email_address.get(email, 0) + 1

lst = []
for key, value in email_address.items():
    lst.append((value, key))

lst.sort(reverse=True)
person_tuple = lst[0]
print(person_tuple[1], person_tuple[0])
'''

'''
filename = input("Enter a file name: ")
fhand = open(filename, 'r')
#print(fhand.read())

sorted = {}
tup_key =()
tup_value = ()
for line in fhand:
    if line.startswith('From '):
        line = line.rstrip()
        #print(line)
        time = line.split()[5]
        hour = time.split(":")[0]
        print(time)
        print(hour)
        sorted[hour]=sorted.get(hour,0) + 1
        print(sorted[hour])

lst = list(sorted.items())
lst.sort()

for t in lst:
    print(t[0], t[1])
'''
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
file = input("Enter a file name: ")
fhand = open(file, 'r')

lst = {}

inp = fhand.read()
print(len(inp))

for n in inp.lower():
    if n in alphabet:
        lst[n] = lst.get(n, 0) + 1

sorted = list(lst.keys())
sorted.sort()

sd = {i: lst[i] for i in sorted}
print(sd)
'''
'''
filename = input("Enter a file name: ")
fhand = open(filename, 'r')

d={}

for n in fhand:
    if n.startswith('From '):
        day = n.split()[2]
        d[day] = d.get(day, 0) + 1
print(d)
'''
'''
filename = input("Enter a file name: ")
fhand = open(filename, 'r')

d={}

for n in fhand:
    if n.startswith('From:'):
        sender = n.split()[1]
        d[sender] = d.get(sender, 0) + 1
print(d)
max = max(d, key=d.get)
print(max)

print("Maximum msgs are for:",max)
'''

filename = input("Enter a file name: ")
fhand = open(filename, 'r')

d={}

for n in fhand:
    if n.startswith('From:'):
        #sender = n.split()[1]
        #domain = sender.split("@")[1]
        domain = n.split()[1].split("@")[1]
        d[domain] = d.get(domain, 0) + 1
print(d)










































































