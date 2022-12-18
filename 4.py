import re
with open("data/4.txt", "r") as f:
    data = f.readlines()

list1 = [x.replace("\n", "") for x in data]
list2 = [x.split(", ") for x in list1]

list3 = list()
for x in list2:
   for y in x:
        a = (re.findall(r'\d+', y))
        b = [int(x) for x in a]
        set_a = set()
        set_b = set()
        for number in range(b[0], b[1]+1):
            set_a.add(number)
        for number in range(b[2], b[3]+1):
            set_b.add(number)
        list3.append([set_a, set_b])

i = 0
for x in list3:
    if x[0].issubset(x[1]) or x[1].issubset(x[0]):
        i+=1
print(f"Part one: {i}")

poc=0
for x in list3:
    
    if x[0].intersection(x[1]):
        poc+=1

print(f"Part two: {poc}")