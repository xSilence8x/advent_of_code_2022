"""
Every three lines are a single group.
Get an intersection character of the lines.
Get the sum as in part no. one.
"""
with open("data/3.txt", "r") as f:
    data = f.readlines()

list1 = [x.replace("\n", "") for x in data]

list2 = [list1[x:x + 3] for x in range(0, len(list1), 3)]

list3 = []
for x in list2:
    set_a = set()
    set_b = set()
    set_c = set()
    for letter in x[0]:
        set_a.add(letter)
    for letter in x[1]:
        set_b.add(letter)
    for letter in x[2]:
        set_c.add(letter)
    list3.append([set_a, set_b, set_c])

list4 = [x[0].intersection(x[1], x[2]) for x in list3] 

list5 = [x.pop() for x in list4]

list6 = [ord(x)-96 if x.islower() else ord(x)-38 for x in list5]

print(f"The sum is: {sum(list6)}")
