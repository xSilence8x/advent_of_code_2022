with open("data/6.txt", "r") as f:
    data = f.readline()


# print(data)
i = 0

string = str()
for letter in data:
    i += 1
    string += letter
    if len(string) == 4:
        #print(string, i)
        repeated = len(set(string)) != len(string)
        if repeated:
            string = string[1:]
            #print(string)
        else:
            print(f"The string is: {string} and index: {i}")
            break
