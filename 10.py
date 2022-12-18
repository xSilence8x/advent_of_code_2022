with open("data/10.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

start_value = 1
cycle_count = 0
cycle_check = [20, 60, 100, 140, 180, 220]
cycle_multi_result = []

for element in data:
    if element == "noop":
        cycle_count += 1
        if cycle_count in cycle_check:
            cycle_multi_result.append(cycle_count * start_value)
        
    else:
        action, amount = element.split(" ")
        for number in range(2):
            cycle_count += 1
            if cycle_count in cycle_check:
                cycle_multi_result.append(cycle_count * start_value)
        start_value += int(amount)

print(f"Total of cycles: {sum(cycle_multi_result)}")