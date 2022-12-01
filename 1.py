from itertools import groupby

with open("1.txt", "r") as f:
    text = f.readlines()

list1 = [x.replace("\n", "") for x in text]

list2 = [list(sub) for ele, sub in groupby(list1, key = bool) if ele]

list3 = [[int(y) for y in x]for x in list2]

list_of_results = [sum(x) for x in list3]

print(f"The highest score is {max(list_of_results)}")

test_list = list_of_results

three_highest = []
for x in range(3):
    print(f"Three highest calories on pos 1-3: {max(test_list)}")
    three_highest.append(max(test_list))
    test_list.remove(max(test_list))

print(f"The sum of three highest calories is: {sum(three_highest)}")