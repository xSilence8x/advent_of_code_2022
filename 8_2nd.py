with open("data/8.txt", "r") as f:
    #data = [line.replace("\n", "") for line in f.readlines()]
    data = [line.strip() for line in f.readlines()]

line_count = 0
tab_soucinu = []

for line in data: # go through lines
    
    number_count = 0
    for number in line: # check every number
        if (line_count > 0 and number_count > 0) and (line_count < len(data)-1 and number_count < len(line)-1): # checks only inside numbers
            a = data[line_count-1][number_count]
            b = data[line_count][number_count-1]
            c = data[line_count][number_count+1]
            d = data[line_count+1][number_count]
            
            if int(number) >= int(a) or int(number) >= int(b) or int(number) >= int(c) or int(number) >= int(d):
                count_a = 0
                count_b = 0
                count_c = 0
                count_d = 0
                print(f"radek {line_count+1}, cislo {number}")
                if int(number) >= int(a):
                    for i in range(line_count):
                        new_a = int(data[line_count-1-i][number_count])
                        if i == line_count-1:
                            count_a += 1
                            break
                        elif int(number) > new_a:
                            count_a += 1
                            continue
                        elif int(number) == new_a or int(number) < new_a:
                            count_a += 1
                            break
                        else:
                            break
                if int(number) >= int(b):
                    for i in range(number_count):
                        new_b = int(data[line_count][number_count-1-i])
                        if i == number_count-1:
                            count_b += 1
                            break
                        elif int(number) > new_b:
                            count_b += 1
                            continue
                        elif int(number) == new_b or int(number) < new_b:
                            count_b += 1
                            break
                        else:
                            break
                if int(number) >= int(c):
                    for i in range((len(line)-1) - (number_count+1)+1):
                        new_c = int(data[line_count][number_count+1+i])
                        if i == ((len(line)-1) - (number_count+1)):
                            count_c += 1
                            break
                        elif int(number) > new_c:
                            count_c += 1
                            continue
                        elif int(number) == new_c or int(number) < new_c:
                            count_c += 1
                            break
                        else:
                            break
                if int(number) >= int(d):
                    for i in range((len(data) - 1)  -(line_count+1)+1):
                        new_d = int(data[line_count+1+i][number_count])
                        if i == ((len(data) - 1)  -(line_count+1)):
                            count_d += 1
                            break
                        elif int(number) > new_d:
                            count_d += 1
                            continue
                        elif int(number) == new_d or int(number) < new_d:
                            count_d += 1
                            break
                        else:
                            break
                print(count_a, count_b, count_c, count_d)
                tab_soucinu.append(count_a * count_b * count_c * count_d)    
        number_count += 1
    line_count += 1

print(max(tab_soucinu))

