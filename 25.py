with open("data/25.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

values = {"0":0, "1":1, "2":2, "-":-1, "=":-2}
snafu_values = ["0", "1", "2", "=", "-"]

my_input = "1-0---0"

def to_decimal(inp, seq):
    reverse_inp = inp[::-1]
    i = 1
    results = []
    for element in reverse_inp:
        results.append(seq[element] * i)
        i *= 5
    return sum(results)

final_results = [to_decimal(snafu, values) for snafu in data]
decimal_sum = sum(final_results)   


def to_snafu(inp, seq):
    result = []
    while inp > 0:
        remainer = inp % 5
        result.append(seq[remainer])
        inp = (2 + inp)  // 5
    return "".join(result[::-1])

print(f"Part one result: {to_snafu(decimal_sum, snafu_values)}")

