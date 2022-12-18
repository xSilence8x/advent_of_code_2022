with open("data/8.txt", "r") as f:
    #data = [line.replace("\n", "") for line in f.readlines()]
    data = [line.strip() for line in f.readlines()]

line_count = 0
trees_count = 0

for line in data: # go through lines
    number_count = 0
    for number in line: # check every number
        if line_count == 0: # on 1st line take every number
            trees_count += 1
        if (line_count > 0 and line_count < len(line)-1) & (number_count == 0 or number_count == len(line)-1):
            trees_count += 1
        if (line_count > 0 and number_count > 0) and (line_count < len(data)-1 and number_count < len(line)-1): # checks only inside numbers
            a = data[line_count-1][number_count]
            b = data[line_count][number_count-1]
            c = data[line_count][number_count+1]
            d = data[line_count+1][number_count]
            """"""
            if int(number) > int(a) or int(number) > int(b) or int(number) > int(c) or int(number) > int(d):
                cond = True
                while cond:
                    if int(number) > int(a):
                        for i in range(line_count):
                            new_a = int(data[line_count-1-i][number_count])
                            
                            if int(number) > new_a and i == line_count-1:
                                trees_count += 1
                                cond = False
                                break
                            elif int(number) > new_a:
                                continue
                            else:
                                break
                    if int(number) > int(b) and cond:
                        for i in range(number_count):
                            new_b = int(data[line_count][number_count-1-i])
                            if int(number) > new_b and i == number_count-1:
                                trees_count += 1
                                cond = False
                                break
                            elif int(number) > new_b:
                                continue
                            else:
                                break
                    if int(number) > int(c) and cond:
                        for i in range((len(line)-1) - (number_count+1)+1):
                            new_c = int(data[line_count][number_count+1+i])
                            if int(number) > new_c and i == ((len(line)-1) - (number_count+1)):
                                trees_count += 1
                                cond = False
                                break
                            elif int(number) > new_c:
                                continue
                            else:
                                break
                    if int(number) > int(d) and cond:
                        for i in range((len(data) - 1)  -(line_count+1)+1):
                            new_d = int(data[line_count+1+i][number_count])
                            if int(number) > new_d and i == ((len(data) - 1)  -(line_count+1)):
                                trees_count += 1
                                cond = False
                                break
                            elif int(number) > new_d:
                                continue
                            else:
                                break
                    cond = False
            """"""
        if line_count == len(line)-1: # on last line take every number
            trees_count += 1
        number_count += 1
    line_count += 1
print(f"{trees_count} trees are visible.")

