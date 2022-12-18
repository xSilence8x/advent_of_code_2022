moves = []
count = 0

with open("data/5.txt", "r") as f:
    data = f.readlines()

for line in data:
    element = []
    count = count + 1
    if count > 10: # line for list moves
        for x in line.strip().split(" "):
            element.append(x)
        moves.append(element)

listx = []

# takes the letters until n-th line
count2 = 0
for line in data:
    count2 += 1
    if count2 < 9:
        for letter in line[1:len(line):4]: # takes every 4th ascii
            listx.append(letter)


list1 = list(listx[0::9])
list2 = list(listx[1::9])
list3 = list(listx[2::9])
list4 = list(listx[3::9])
list5 = list(listx[4::9])
list6 = list(listx[5::9])
list7 = list(listx[6::9])
list8 = list(listx[7::9])
list9 = list(listx[8::9])

stacks = [list1, list2, list3, list4, list5, list6, list7, list8, list9]

for x in stacks:
    x.reverse()
    while " " in x:
        x.remove(" ")

print(stacks)

"""
Part 1:
"""

# for item in moves:
#     from_stack = int(item[3])
#     to_stack = int(item[5])
#     for x in range(int(item[1])):
#         letter = stacks[from_stack-1][-1]
#         del(stacks[from_stack-1][-1])
#         stacks[to_stack-1].append(letter)

# solution = " "

# for stack in stacks:
#     solution += stack[-1]

# print(f"Your solution is: {solution}")

"""
Part 2:
"""

for item in moves:
    from_stack = int(item[3])
    to_stack = int(item[5])
    helping_stack = []
    for x in range(int(item[1])):
        letter = stacks[from_stack-1][-1]
        del(stacks[from_stack-1][-1])
        helping_stack.insert(0, letter)
    for letter in helping_stack:
        stacks[to_stack-1].append(letter)

solution2 = " "
for stack in stacks:
    solution2 += stack[-1]

print(f"Your solution of part 2 is: {solution2}")