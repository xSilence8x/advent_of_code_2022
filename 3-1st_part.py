"""
Divide every line into two halves.
Get an intersection character of two these two sets.
Convert the character to priority:
    a–z: 1–26
    A–Z: 27–52
Sum the converted priorities.
"""
with open("data/3.txt", "r") as f:
    data = f.readlines()

list1 = [x.replace("\n", "") for x in data]

list2 = list()
for x in list1:
    length = len(x)
    middle_ind = length // 2
    first_half = x[:middle_ind]
    second_half = x[middle_ind:]
    set_a = set()
    set_b = set()
    for letter in first_half:
        set_a.add(letter)
    for letter in second_half:
        set_b.add(letter)
    list2.append([set_a, set_b])

list3 = [x[0].intersection(x[1]) for x in list2]   

list4 = [x.pop() for x in list3]

list5 = [ord(x)-96 if x.islower() else ord(x)-38 for x in list4]

print(f"The sum is: {sum(list5)}")